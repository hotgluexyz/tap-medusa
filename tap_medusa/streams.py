"""Stream type classes for tap-medusa."""

from singer_sdk import typing as th

from tap_medusa.client import MedusaStream

profile = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
    th.Property("name", th.StringType),
    th.Property("type", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
)

address = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
    th.Property("customer_id", th.StringType),
    th.Property("company", th.StringType),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("address_1", th.StringType),
    th.Property("address_2", th.StringType),
    th.Property("city", th.StringType),
    th.Property("country_code", th.StringType),
    th.Property("province", th.StringType),
    th.Property("postal_code", th.StringType),
    th.Property("phone", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
)

item = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("cart_id", th.StringType),
    th.Property("order_id", th.StringType),
    th.Property("swap_id", th.StringType),
    th.Property("claim_order_id", th.StringType),
    th.Property("original_item_id", th.StringType),
    th.Property("order_edit_id", th.StringType),
    th.Property("title", th.StringType),
    th.Property("description", th.StringType),
    th.Property("thumbnail", th.StringType),
    th.Property("is_return", th.BooleanType),
    th.Property("is_giftcard", th.BooleanType),
    th.Property("should_merge", th.BooleanType),
    th.Property("allow_discounts", th.BooleanType),
    th.Property("has_shipping", th.BooleanType),
    th.Property("unit_price", th.NumberType),
    th.Property("variant_id", th.StringType),
    th.Property("quantity", th.IntegerType),
    th.Property("fulfilled_quantity", th.IntegerType),
    th.Property("returned_quantity", th.IntegerType),
    th.Property("shipped_quantity", th.IntegerType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property(
        "product",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("created_at", th.DateTimeType),
            th.Property("updated_at", th.DateTimeType),
            th.Property("deleted_at", th.DateTimeType),
            th.Property("title", th.StringType),
            th.Property("subtitle", th.StringType),
            th.Property("description", th.StringType),
            th.Property("handle", th.StringType),
            th.Property("is_giftcard", th.BooleanType),
            th.Property("status", th.StringType),
            th.Property("thumbnail", th.StringType),
            th.Property("weight", th.NumberType),
            th.Property("length", th.NumberType),
            th.Property("height", th.NumberType),
            th.Property("width", th.NumberType),
            th.Property("hs_code", th.StringType),
            th.Property("origin_country", th.StringType),
            th.Property("mid_code", th.StringType),
            th.Property("material", th.StringType),
            th.Property("collection_id", th.StringType),
            th.Property("type_id", th.StringType),
            th.Property("discountable", th.BooleanType),
            th.Property("external_id", th.StringType),
            th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
            th.Property("profiles", th.ArrayType(profile)),
            th.Property("profile", profile),
            th.Property("profile_id", th.StringType),
        ),
    ),
    th.Property("refundable", th.IntegerType),
)

shipping_method = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("shipping_option_id", th.StringType),
    th.Property("order_id", th.StringType),
    th.Property("claim_order_id", th.StringType),
    th.Property("cart_id", th.StringType),
    th.Property("swap_id", th.StringType),
    th.Property("return_id", th.StringType),
    th.Property("price", th.NumberType),
    th.Property("data", th.CustomType({"type": ["object", "string"]})),
    th.Property(
        "shipping_option",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("created_at", th.DateTimeType),
            th.Property("updated_at", th.DateTimeType),
            th.Property("deleted_at", th.DateTimeType),
            th.Property("name", th.StringType),
            th.Property("region_id", th.StringType),
            th.Property("profile_id", th.StringType),
            th.Property("provider_id", th.StringType),
            th.Property("price_type", th.StringType),
            th.Property("amount", th.NumberType),
            th.Property("is_return", th.BooleanType),
            th.Property("admin_only", th.BooleanType),
            th.Property("data", th.CustomType({"type": ["object", "string"]})),
            th.Property(
                "metadata",
                th.CustomType({"type": ["object", "string"]}),
            ),
        ),
    ),
    th.Property(
        "tax_lines",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("created_at", th.DateTimeType),
                th.Property("updated_at", th.DateTimeType),
                th.Property("rate", th.NumberType),
                th.Property("name", th.StringType),
                th.Property("code", th.StringType),
                th.Property(
                    "metadata",
                    th.CustomType({"type": ["object", "string"]}),
                ),
                th.Property("shipping_method_id", th.StringType),
            )
        ),
    ),
)


class ProductsStream(MedusaStream):
    """Define custom stream."""

    name = "products"
    path = "/products"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$.products[*]"
    additional_params = {
        "expand": "images,options,options.values,profiles,sales_channels,tags,variants.options,variants.prices,collection,categories"
    }
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("deleted_at", th.DateTimeType),
        th.Property("title", th.StringType),
        th.Property("subtitle", th.StringType),
        th.Property("description", th.StringType),
        th.Property("handle", th.StringType),
        th.Property("is_giftcard", th.BooleanType),
        th.Property("status", th.StringType),
        th.Property("thumbnail", th.StringType),
        th.Property("weight", th.NumberType),
        th.Property("length", th.NumberType),
        th.Property("height", th.NumberType),
        th.Property("width", th.NumberType),
        th.Property("hs_code", th.StringType),
        th.Property("origin_country", th.StringType),
        th.Property("mid_code", th.StringType),
        th.Property("material", th.StringType),
        th.Property("type_id", th.StringType),
        th.Property("discountable", th.BooleanType),
        th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
        th.Property(
            "categories", th.ArrayType(th.CustomType({"type": ["object", "string"]}))
        ),
        th.Property(
            "collection",
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("created_at", th.DateTimeType),
                th.Property("updated_at", th.DateTimeType),
                th.Property("deleted_at", th.DateTimeType),
                th.Property("title", th.StringType),
                th.Property("subtitle", th.StringType),
                th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
            ),
        ),
        th.Property("collection_id", th.StringType),
        th.Property(
            "images",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("created_at", th.DateTimeType),
                    th.Property("updated_at", th.DateTimeType),
                    th.Property("deleted_at", th.DateTimeType),
                    th.Property("url", th.StringType),
                    th.Property(
                        "metadata", th.CustomType({"type": ["object", "string"]})
                    ),
                )
            ),
        ),
        th.Property(
            "options",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("created_at", th.DateTimeType),
                    th.Property("updated_at", th.DateTimeType),
                    th.Property("deleted_at", th.DateTimeType),
                    th.Property("title", th.StringType),
                    th.Property("product_id", th.StringType),
                    th.Property(
                        "metadata", th.CustomType({"type": ["object", "string"]})
                    ),
                    th.Property(
                        "values",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("id", th.StringType),
                                th.Property("created_at", th.DateTimeType),
                                th.Property("updated_at", th.DateTimeType),
                                th.Property("deleted_at", th.DateTimeType),
                                th.Property("value", th.StringType),
                                th.Property("option_id", th.StringType),
                                th.Property("variant_id", th.StringType),
                                th.Property("metadata", th.StringType),
                            )
                        ),
                    ),
                )
            ),
        ),
        th.Property("profiles", th.ArrayType(profile)),
        th.Property("profile", profile),
        th.Property("profile_id", th.StringType),
        th.Property(
            "sales_channels",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("created_at", th.DateTimeType),
                    th.Property("updated_at", th.DateTimeType),
                    th.Property("deleted_at", th.DateTimeType),
                    th.Property("name", th.StringType),
                    th.Property("description", th.StringType),
                    th.Property("is_disabled", th.BooleanType),
                    th.Property(
                        "metadata", th.CustomType({"type": ["object", "string"]})
                    ),
                )
            ),
        ),
        th.Property(
            "tags", th.ArrayType(th.CustomType({"type": ["object", "string"]}))
        ),
        th.Property("type", th.StringType),
        th.Property("type", th.StringType),
        th.Property(
            "variants",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("created_at", th.DateTimeType),
                    th.Property("updated_at", th.DateTimeType),
                    th.Property("deleted_at", th.DateTimeType),
                    th.Property("title", th.StringType),
                    th.Property("product_id", th.StringType),
                    th.Property("sku", th.StringType),
                    th.Property("barcode", th.StringType),
                    th.Property("ean", th.StringType),
                    th.Property("upc", th.StringType),
                    th.Property("variant_rank", th.NumberType),
                    th.Property("inventory_quantity", th.NumberType),
                    th.Property("allow_backorder", th.BooleanType),
                    th.Property("manage_inventory", th.BooleanType),
                    th.Property("hs_code", th.StringType),
                    th.Property("origin_country", th.StringType),
                    th.Property("mid_code", th.StringType),
                    th.Property("material", th.StringType),
                    th.Property("weight", th.NumberType),
                    th.Property("length", th.NumberType),
                    th.Property("height", th.NumberType),
                    th.Property("width", th.NumberType),
                    th.Property(
                        "metadata", th.CustomType({"type": ["object", "string"]})
                    ),
                    th.Property(
                        "options",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("id", th.StringType),
                                th.Property("created_at", th.DateTimeType),
                                th.Property("updated_at", th.DateTimeType),
                                th.Property("deleted_at", th.DateTimeType),
                                th.Property("value", th.StringType),
                                th.Property("option_id", th.StringType),
                                th.Property("variant_id", th.StringType),
                                th.Property(
                                    "metadata",
                                    th.CustomType({"type": ["object", "string"]}),
                                ),
                            )
                        ),
                    ),
                    th.Property(
                        "prices",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("id", th.StringType),
                                th.Property("created_at", th.DateTimeType),
                                th.Property("updated_at", th.DateTimeType),
                                th.Property("deleted_at", th.DateTimeType),
                                th.Property("currency_code", th.StringType),
                                th.Property("amount", th.NumberType),
                                th.Property("min_quantity", th.NumberType),
                                th.Property("max_quantity", th.NumberType),
                                th.Property("price_list_id", th.StringType),
                                th.Property("region_id", th.StringType),
                                th.Property("price_list", th.NumberType),
                                th.Property("variant_id", th.StringType),
                            )
                        ),
                    ),
                    th.Property("original_price", th.NumberType),
                    th.Property("calculated_price", th.NumberType),
                    th.Property("original_price_incl_tax", th.NumberType),
                    th.Property("calculated_price_incl_tax", th.NumberType),
                    th.Property("original_tax", th.NumberType),
                    th.Property("calculated_tax", th.NumberType),
                    th.Property("tax_rates", th.StringType),
                )
            ),
        ),
    ).to_dict()


class OrdersStream(MedusaStream):
    """Define custom stream."""

    name = "orders"
    path = "/orders"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$.orders[*]"
    additional_params = {
        "fields": "id,updated_at,status,fulfillment_status,payment_status,display_id,cart_id,customer_id,email,region_id,currency_code,tax_rate,draft_order_id,canceled_at,no_notification,sales_channel_id,metadata,external_id"
    }
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("external_id", th.StringType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("status", th.StringType),
        th.Property("fulfillment_status", th.StringType),
        th.Property("payment_status", th.StringType),
        th.Property("display_id", th.IntegerType),
        th.Property("cart_id", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("email", th.StringType),
        th.Property("region_id", th.StringType),
        th.Property("currency_code", th.StringType),
        th.Property("tax_rate", th.StringType),
        th.Property("draft_order_id", th.StringType),
        th.Property("canceled_at", th.DateTimeType),
        th.Property("no_notification", th.StringType),
        th.Property("sales_channel_id", th.StringType),
        th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
        th.Property("billing_address", address),
        th.Property(
            "claims", th.ArrayType(th.CustomType({"type": ["object", "string"]}))
        ),
        th.Property(
            "customer",
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("created_at", th.DateTimeType),
                th.Property("updated_at", th.DateTimeType),
                th.Property("deleted_at", th.DateTimeType),
                th.Property("email", th.StringType),
                th.Property("first_name", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("billing_address_id", th.StringType),
                th.Property("phone", th.StringType),
                th.Property("has_account", th.BooleanType),
                th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
            ),
        ),
        th.Property(
            "discounts", th.ArrayType(th.CustomType({"type": ["object", "string"]}))
        ),
        th.Property(
            "fulfillments", th.ArrayType(th.CustomType({"type": ["object", "string"]}))
        ),
        th.Property(
            "gift_card_transactions",
            th.ArrayType(th.CustomType({"type": ["object", "string"]})),
        ),
        th.Property(
            "gift_cards", th.ArrayType(th.CustomType({"type": ["object", "string"]}))
        ),
        th.Property("items", th.ArrayType(item)),
        th.Property(
            "payments",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("created_at", th.DateTimeType),
                    th.Property("updated_at", th.DateTimeType),
                    th.Property("swap_id", th.StringType),
                    th.Property("cart_id", th.StringType),
                    th.Property("order_id", th.StringType),
                    th.Property("amount", th.NumberType),
                    th.Property("currency_code", th.StringType),
                    th.Property("amount_refunded", th.NumberType),
                    th.Property("provider_id", th.StringType),
                    th.Property("captured_at", th.DateTimeType),
                    th.Property("canceled_at", th.DateTimeType),
                    th.Property("metadata", th.StringType),
                    th.Property("idempotency_key", th.StringType),
                    th.Property("data", th.CustomType({"type": ["object", "string"]})),
                )
            ),
        ),
        th.Property(
            "refunds", th.ArrayType(th.CustomType({"type": ["object", "string"]}))
        ),
        th.Property(
            "region",
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("created_at", th.DateTimeType),
                th.Property("updated_at", th.DateTimeType),
                th.Property("deleted_at", th.DateTimeType),
                th.Property("name", th.StringType),
                th.Property("currency_code", th.StringType),
                th.Property("tax_rate", th.NumberType),
                th.Property("tax_code", th.StringType),
                th.Property("gift_cards_taxable", th.BooleanType),
                th.Property("automatic_taxes", th.BooleanType),
                th.Property("tax_provider_id", th.StringType),
                th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
            ),
        ),
        th.Property(
            "returns", th.ArrayType(th.CustomType({"type": ["object", "string"]}))
        ),
        th.Property(
            "sales_channel",
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("created_at", th.DateTimeType),
                th.Property("updated_at", th.DateTimeType),
                th.Property("deleted_at", th.StringType),
                th.Property("name", th.StringType),
                th.Property("description", th.StringType),
                th.Property("is_disabled", th.BooleanType),
                th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
            ),
        ),
        th.Property("shipping_address", address),
        th.Property("shipping_methods", th.ArrayType(shipping_method)),
        th.Property(
            "returns", th.ArrayType(th.CustomType({"type": ["object", "string"]}))
        ),
        th.Property(
            "swaps", th.ArrayType(th.CustomType({"type": ["object", "string"]}))
        ),
        th.Property("subtotal", th.NumberType),
        th.Property("discount_total", th.NumberType),
        th.Property("shipping_total", th.NumberType),
        th.Property("refunded_total", th.NumberType),
        th.Property("paid_total", th.NumberType),
        th.Property("refundable_amount", th.NumberType),
        th.Property("item_tax_total", th.NumberType),
        th.Property("shipping_tax_total", th.NumberType),
        th.Property("tax_total", th.NumberType),
        th.Property("gift_card_total", th.NumberType),
        th.Property("gift_card_tax_total", th.NumberType),
        th.Property("total", th.NumberType),
    ).to_dict()


class ReturnsStream(MedusaStream):
    """Define custom stream."""

    name = "returns"
    path = "/returns"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.returns[*]"
    additional_params = {}

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("status", th.StringType),
        th.Property("swap_id", th.StringType),
        th.Property("claim_order_id", th.StringType),
        th.Property("order_id", th.StringType),
        th.Property("shipping_data", th.CustomType({"type": ["object", "string"]})),
        th.Property("location_id", th.StringType),
        th.Property("refund_amount", th.NumberType),
        th.Property("no_notification", th.BooleanType),
        th.Property("idempotency_key", th.StringType),
        th.Property("received_at", th.DateTimeType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
        th.Property("items", th.ArrayType(item)),
        th.Property("swap", th.CustomType({"type": ["object", "string"]})),
        th.Property("claim_order", th.CustomType({"type": ["object", "string"]})),
        th.Property("order", th.CustomType({"type": ["object", "string"]})),
        th.Property("shipping_method", shipping_method),
    ).to_dict()
