"""Medusa tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_medusa.streams_v1 import OrdersStream as OrdersStreamV1, ProductsStream as ProductsStreamV1, ReturnsStream as ReturnsStreamV1


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
        th.Property(
            "medusa_v2",
            th.BooleanType,
            default=False,
            description="Use Medusa v2 API schemas when True, v1 schemas when False",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        if self.config.get("medusa_v2", False):
            from tap_medusa.streams_v2 import OrdersStream as OrdersStreamV2, ProductsStream as ProductsStreamV2, ReturnsStream as ReturnsStreamV2
            stream_types = [OrdersStreamV2, ProductsStreamV2, ReturnsStreamV2]
        else:
            stream_types = [OrdersStreamV1, ProductsStreamV1, ReturnsStreamV1]
        
        return [stream_class(tap=self) for stream_class in stream_types]


if __name__ == "__main__":
    TapMedusa.cli()
