"""Medusa tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_medusa.streams import OrdersStream, ProductsStream, ReturnsStream

STREAM_TYPES = [OrdersStream, ProductsStream, ReturnsStream]


class TapMedusa(Tap):
    """Medusa tap class."""

    name = "tap-medusa"

    def __init__(
        self,
        config=None,
        catalog=None,
        state=None,
        parse_env_config=False,
        validate_config=True,
    ) -> None:
        self.config_file = config[0]
        super().__init__(config, catalog, state, parse_env_config, validate_config)

    config_jsonschema = th.PropertiesList(
        th.Property(
            "base_url",
            th.StringType,
            required=True,
        ),
        th.Property(
            "email",
            th.StringType,
        ),
        th.Property(
            "password",
            th.StringType,
        ),
        th.Property(
            "api_key",
            th.StringType,
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapMedusa.cli()
