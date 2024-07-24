"""REST client handling, including MedusaStream base class."""

import datetime
import json
from typing import Any, Dict, Optional, Union

import requests
from memoization import cached
from pendulum import parse
from singer.schema import Schema
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.plugin_base import PluginBase as TapBaseClass
from singer_sdk.streams import RESTStream


class MedusaStream(RESTStream):
    """Medusa stream class."""

    def __init__(
        self,
        tap: TapBaseClass,
        name: Optional[str] = None,
        schema: Optional[Union[Dict[str, Any], Schema]] = None,
        path: Optional[str] = None,
    ) -> None:
        super().__init__(tap, name=name, schema=schema, path=path)

    records_jsonpath = "$[*]"
    user_logged = False
    additional_params = {}

    @property
    def url_base(self):
        base_url = self.config.get("base_url")
        if base_url.endswith("/admin"):
            return self.config.get("base_url")
        else:
            return f'{self.config.get("base_url")}/admin'

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # if api_key auth with api_key
        if self.config.get("api_key"):
            headers["x-medusa-access-token"] = self.config.get("api_key")
        else:
            # add authentication header
            headers["Authorization"] = f"Bearer {self.get_access_token()}"
        return headers
    
    def is_token_valid(self) -> bool:
        access_token = self._tap._config.get("access_token")
        now = round(datetime.datetime.utcnow().timestamp())
        expires_in = self._tap.config.get("expires_in")
        if expires_in is not None:
            expires_in = int(expires_in)
        if not access_token:
            return False
        if not expires_in:
            return False
        return not ((expires_in - now) < 120)

    def get_access_token(self):
        headers = {"Content-Type": "application/json"}
        login_data = {
            "email": self.config.get("email"),
            "password": self.config.get("password"),
        }
        
        access_token = self._tap._config.get("access_token")
        if not self.is_token_valid():
            access_token = requests.post(
                url=f"{self.url_base}/auth/token",
                data=json.dumps(login_data),
                headers=headers,
            )
            self.validate_response(access_token)
            access_token = access_token.json()["access_token"]
            self._tap._config["access_token"] = access_token
            now = round((datetime.datetime.utcnow() + datetime.timedelta(minutes=60)).timestamp())
            self._tap._config["expires_in"] = now

            # write access token in config file
            with open(self._tap.config_file, "w") as outfile:
                json.dump(self._tap._config, outfile, indent=4)

        return access_token

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        previous_token = previous_token or 0
        res_json = response.json()

        records_len = len(list(extract_jsonpath(self.records_jsonpath, res_json)))
        if records_len:
            return previous_token + records_len

    def get_starting_time(self, context):
        start_date = self.config.get("start_date")
        if start_date:
            start_date = parse(self.config.get("start_date"))
        rep_key = self.get_starting_timestamp(context)
        return rep_key or start_date

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if self.additional_params:
            params.update(self.additional_params)
        if next_page_token:
            params["offset"] = next_page_token
        # filter by date
        start_date = self.get_starting_time(context)
        if start_date and self.replication_key:
            start_date = start_date + datetime.timedelta(seconds=1)
            start_date = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
            params[f"{self.replication_key}[gt]"] = start_date
        return params
