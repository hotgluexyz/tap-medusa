"""Stream type classes for tap-medusa-v2."""

from singer_sdk import typing as th

from tap_medusa.client import MedusaStream

product_option_value = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("value", th.StringType),
    th.Property("option", th.CustomType({"type": ["object", "string"]})),
    th.Property("option_id", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
)
product_option = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("title", th.StringType),
    th.Property("product", th.CustomType({"type": ["object", "string"]})),
    th.Property("product_id", th.StringType),
    th.Property("values", th.ArrayType(product_option_value)),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
)

variant_option_value = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("value", th.StringType),
    th.Property("option", th.CustomType({"type": ["object", "string"]})),
    th.Property("option_id", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
)

calculated_price = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("calculated_amount", th.NumberType),
    th.Property("original_amount", th.NumberType),
    th.Property("currency_code", th.StringType),
    th.Property("original_amount_with_tax", th.NumberType),
    th.Property("original_amount_without_tax", th.NumberType),
    th.Property("is_calculated_price_price_list", th.BooleanType),
    th.Property("is_calculated_price_tax_inclusive", th.BooleanType),
    th.Property("calculated_amount_with_tax", th.NumberType),
    th.Property("calculated_amount_without_tax", th.NumberType),
    th.Property("is_original_price_price_list", th.BooleanType),
    th.Property("is_original_price_tax_inclusive", th.BooleanType),
    th.Property("calculated_price", th.CustomType({"type": ["object", "string"]})),
    th.Property("original_price", th.CustomType({"type": ["object", "string"]})),
)

product_variant = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("title", th.StringType),
    th.Property("sku", th.StringType),
    th.Property("barcode", th.StringType),
    th.Property("ean", th.StringType),
    th.Property("upc", th.StringType),
    th.Property("product_id", th.StringType),
    th.Property("inventory_quantity", th.NumberType),
    th.Property("allow_backorder", th.BooleanType),
    th.Property("manage_inventory", th.BooleanType),
    th.Property("variant_rank", th.NumberType),
    th.Property("weight", th.NumberType),
    th.Property("length", th.NumberType),
    th.Property("height", th.NumberType),
    th.Property("width", th.NumberType),
    th.Property("origin_country", th.StringType),
    th.Property("hs_code", th.StringType),
    th.Property("mid_code", th.StringType),
    th.Property("material", th.StringType),
    th.Property("options", th.ArrayType(variant_option_value)),
    th.Property("product", th.CustomType({"type": ["object", "string"]})),
    th.Property("calculated_price", calculated_price),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
)

product_image = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("url", th.StringType),
    th.Property("rank", th.NumberType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
)

product_type = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("value", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
)

product_collection = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("title", th.StringType),
    th.Property("handle", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("products", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
)

product_tag = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("value", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
)

class ProductsStream(MedusaStream):
    """Define custom stream."""

    name = "products"
    path = "/products"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$.products[*]"

    additional_params = {
        "fields": "id"
    }

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("title", th.StringType),
        th.Property("subtitle", th.StringType),
        th.Property("description", th.StringType),
        th.Property("handle", th.StringType),
        th.Property("status", th.StringType),
        th.Property("thumbnail", th.StringType),
        th.Property("is_giftcard", th.BooleanType),
        th.Property("collection_id", th.StringType),
        th.Property("type_id", th.StringType),
        th.Property("external_id", th.StringType),
        th.Property("discountable", th.BooleanType),
        th.Property("weight", th.NumberType),
        th.Property("length", th.NumberType),
        th.Property("height", th.NumberType),
        th.Property("width", th.NumberType),
        th.Property("origin_country", th.StringType),
        th.Property("hs_code", th.StringType),
        th.Property("mid_code", th.StringType),
        th.Property("material", th.StringType),
        th.Property("variants", th.ArrayType(product_variant)),
        th.Property("options", th.ArrayType(product_option)),
        th.Property("images", th.ArrayType(product_image)),
        th.Property("categories", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
        th.Property("tags", th.ArrayType(product_tag)),
        th.Property("collection", product_collection),
        th.Property("type", product_type),
        th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("deleted_at", th.DateTimeType),
        th.Property("sales_channels", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
    ).to_dict()

    def fetch_product_details(self, product_id: str) -> dict:
        """Fetch complete order details including full address information.
        
        Args:
            product_id: The ID of the product to fetch
            
        Returns:
            Complete product data with expanded address details
        """
        url = f"{self.url_base}/products/{product_id}"
        headers = self.http_headers
        params = {
            "fields": "*categories"
        }
        
        try:
            response = self.requests_session.get(url, headers=headers, timeout=self.timeout, params=params)
            self.validate_response(response)
            product_data = response.json()
            return product_data.get("product", {})
        except Exception as e:
            self.logger.warning(f"Failed to fetch product details for product {product_id}: {e}")
            return {}

    def post_process(self, row: dict, context: dict = None) -> dict:
        """Post-process each product record to fetch complete details.
        
        Args:
            row: The product record from the list endpoint
            context: Stream context
            
        Returns:
            Enriched product record with complete address details
        """
        product_id = row.get("id")
        if not product_id:
            return row
        self.logger.info(f"Fetching complete product details for product {product_id}")
        complete_product = self.fetch_product_details(product_id)
        
        if complete_product:
            return complete_product
        else:
            return row


order_summary = th.ObjectType(
    th.Property("paid_total", th.NumberType),
    th.Property("refunded_total", th.NumberType),
    th.Property("pending_difference", th.NumberType),
    th.Property("current_order_total", th.NumberType),
    th.Property("original_order_total", th.NumberType),
    th.Property("transaction_total", th.NumberType),
    th.Property("accounting_total", th.NumberType),
)

order_address = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("address_name", th.StringType),
    th.Property("is_default_shipping", th.BooleanType),
    th.Property("is_default_billing", th.BooleanType),
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
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
)

order_customer = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("email", th.StringType),
    th.Property("default_billing_address_id", th.StringType),
    th.Property("default_shipping_address_id", th.StringType),
    th.Property("company_name", th.StringType),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("phone", th.StringType),
    th.Property("addresses", th.ArrayType(order_address)),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
)

country = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("iso_2", th.StringType),
    th.Property("iso_3", th.StringType),
    th.Property("num_code", th.StringType),
    th.Property("name", th.StringType),
    th.Property("display_name", th.StringType),
)

payment_provider = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("is_enabled", th.BooleanType),
)

order_region = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("currency_code", th.StringType),
    th.Property("automatic_taxes", th.BooleanType),
    th.Property("countries", th.ArrayType(country)),
    th.Property("payment_providers", th.ArrayType(payment_provider)),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
)

order_shipping_address = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("customer_id", th.StringType),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("phone", th.StringType),
    th.Property("company", th.StringType),
    th.Property("address_1", th.StringType),
    th.Property("address_2", th.StringType),
    th.Property("city", th.StringType),
    th.Property("country_code", th.StringType),
    th.Property("country", country),
    th.Property("province", th.StringType),
    th.Property("postal_code", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
)

order_billing_address = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("customer_id", th.StringType),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("phone", th.StringType),
    th.Property("company", th.StringType),
    th.Property("address_1", th.StringType),
    th.Property("address_2", th.StringType),
    th.Property("city", th.StringType),
    th.Property("country_code", th.StringType),
    th.Property("country", country),
    th.Property("province", th.StringType),
    th.Property("postal_code", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
)

payment_collection = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("currency_code", th.StringType),
    th.Property("amount", th.NumberType),
    th.Property("status", th.StringType),
    th.Property("payment_providers", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
    th.Property("authorized_amount", th.NumberType),
    th.Property("captured_amount", th.NumberType),
    th.Property("refunded_amount", th.NumberType),
    th.Property("completed_at", th.DateTimeType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("payment_sessions", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
    th.Property("payments", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
)

order_shipping_method = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("order_id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("description", th.StringType),
    th.Property("amount", th.NumberType),
    th.Property("is_tax_inclusive", th.BooleanType),
    th.Property("shipping_option_id", th.StringType),
    th.Property("data", th.CustomType({"type": ["object", "string"]})),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("original_total", th.NumberType),
    th.Property("original_subtotal", th.NumberType),
    th.Property("original_tax_total", th.NumberType),
    th.Property("total", th.NumberType),
    th.Property("subtotal", th.NumberType),
    th.Property("tax_total", th.NumberType),
    th.Property("discount_total", th.NumberType),
    th.Property("discount_tax_total", th.NumberType),
    th.Property("tax_lines", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
    th.Property("adjustments", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
    th.Property("detail", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
)

order_item = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("title", th.StringType),
    th.Property("subtitle", th.StringType),
    th.Property("thumbnail", th.StringType),
    th.Property("variant_id", th.StringType),
    th.Property("product_id", th.StringType),
    th.Property("product_title", th.StringType),
    th.Property("product_description", th.StringType),
    th.Property("product_subtitle", th.StringType),
    th.Property("product_type", th.StringType),
    th.Property("product_collection", th.StringType),
    th.Property("product_handle", th.StringType),
    th.Property("variant_sku", th.StringType),
    th.Property("variant_barcode", th.StringType),
    th.Property("variant_title", th.StringType),
    th.Property("variant_option_values", th.CustomType({"type": ["object", "string"]})),
    th.Property("requires_shipping", th.BooleanType),
    th.Property("is_discountable", th.BooleanType),
    th.Property("is_tax_inclusive", th.BooleanType),
    th.Property("unit_price", th.NumberType),
    th.Property("quantity", th.NumberType),
    th.Property("detail", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("original_total", th.NumberType),
    th.Property("original_subtotal", th.NumberType),
    th.Property("original_tax_total", th.NumberType),
    th.Property("item_total", th.NumberType),
    th.Property("item_subtotal", th.NumberType),
    th.Property("item_tax_total", th.NumberType),
    th.Property("total", th.NumberType),
    th.Property("subtotal", th.NumberType),
    th.Property("tax_total", th.NumberType),
    th.Property("discount_total", th.NumberType),
    th.Property("discount_tax_total", th.NumberType),
    th.Property("refundable_total", th.NumberType),
    th.Property("refundable_total_per_unit", th.NumberType),
    th.Property("product_type_id", th.StringType),
    th.Property("variant", th.CustomType({"type": ["object", "string"]})),
    th.Property("product", th.CustomType({"type": ["object", "string"]})),
    th.Property("compare_at_unit_price", th.NumberType),
    th.Property("tax_lines", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
    th.Property("adjustments", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
)

order_fulfillment = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("location_id", th.StringType),
    th.Property("packed_at", th.DateTimeType),
    th.Property("shipped_at", th.DateTimeType),
    th.Property("delivered_at", th.DateTimeType),
    th.Property("canceled_at", th.DateTimeType),
    th.Property("data", th.CustomType({"type": ["object", "string"]})),
    th.Property("provider_id", th.StringType),
    th.Property("shipping_option_id", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("requires_shipping", th.BooleanType),
)

order_transaction = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("order_id", th.StringType),
    th.Property("amount", th.NumberType),
    th.Property("currency_code", th.StringType),
    th.Property("reference", th.StringType),
    th.Property("reference_id", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
)

class OrdersStream(MedusaStream):
    """Define custom stream.
    
    This stream fetches orders from the /admin/orders endpoint and then makes
    subsequent requests to /admin/orders/{order_id} for each order to get
    complete details including full shipping and billing addresses.
    
    Note: In Medusa v2, the list endpoint only returns address IDs, but the
    individual order endpoint returns complete address objects.
    """

    name = "orders"
    path = "/orders"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$.orders[*]"
    
    additional_params = {
        "fields": "id"
    }
    
    schema = th.PropertiesList(
        th.Property("payment_collections", th.ArrayType(payment_collection)),
        th.Property("id", th.StringType),
        th.Property("version", th.NumberType),
        th.Property("region_id", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("sales_channel_id", th.StringType),
        th.Property("email", th.StringType),
        th.Property("currency_code", th.StringType),
        th.Property("items", th.ArrayType(order_item)),
        th.Property("shipping_methods", th.ArrayType(order_shipping_method)),
        th.Property("payment_status", th.StringType),
        th.Property("fulfillment_status", th.StringType),
        th.Property("summary", order_summary),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("original_item_total", th.NumberType),
        th.Property("original_item_subtotal", th.NumberType),
        th.Property("original_item_tax_total", th.NumberType),
        th.Property("item_total", th.NumberType),
        th.Property("item_subtotal", th.NumberType),
        th.Property("item_tax_total", th.NumberType),
        th.Property("original_total", th.NumberType),
        th.Property("original_subtotal", th.NumberType),
        th.Property("original_tax_total", th.NumberType),
        th.Property("total", th.NumberType),
        th.Property("subtotal", th.NumberType),
        th.Property("tax_total", th.NumberType),
        th.Property("discount_total", th.NumberType),
        th.Property("discount_tax_total", th.NumberType),
        th.Property("gift_card_total", th.NumberType),
        th.Property("gift_card_tax_total", th.NumberType),
        th.Property("shipping_total", th.NumberType),
        th.Property("shipping_subtotal", th.NumberType),
        th.Property("shipping_tax_total", th.NumberType),
        th.Property("original_shipping_total", th.NumberType),
        th.Property("original_shipping_subtotal", th.NumberType),
        th.Property("original_shipping_tax_total", th.NumberType),
        th.Property("credit_line_total", th.NumberType),
        th.Property("credit_line_subtotal", th.NumberType),
        th.Property("credit_line_tax_total", th.NumberType),
        th.Property("status", th.StringType),
        th.Property("fulfillments", th.ArrayType(order_fulfillment)),
        th.Property("sales_channel", th.CustomType({"type": ["object", "string"]})),
        th.Property("customer", order_customer),
        th.Property("shipping_address", order_shipping_address),
        th.Property("billing_address", order_billing_address),
        th.Property("display_id", th.NumberType),
        th.Property("transactions", th.ArrayType(order_transaction)),
        th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
        th.Property("region", order_region),
        th.Property("credit_lines", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),

    ).to_dict()

    def fetch_order_details(self, order_id: str) -> dict:
        """Fetch complete order details including full address information.
        
        Args:
            order_id: The ID of the order to fetch
            
        Returns:
            Complete order data with expanded address details
        """
        url = f"{self.url_base}/orders/{order_id}"
        headers = self.http_headers
        params = {
            "fields": "*customer,*sales_channel,*transactions"
        }
        
        try:
            response = self.requests_session.get(url, headers=headers, timeout=self.timeout, params=params)
            self.validate_response(response)
            order_data = response.json()
            return order_data.get("order", {})
        except Exception as e:
            self.logger.warning(f"Failed to fetch order details for order {order_id}: {e}")
            return {}

    def post_process(self, row: dict, context: dict = None) -> dict:
        """Post-process each order record to fetch complete details.
        
        Args:
            row: The order record from the list endpoint
            context: Stream context
            
        Returns:
            Enriched order record with complete address details
        """
        order_id = row.get("id")
        if not order_id:
            return row
        self.logger.info(f"Fetching complete order details for order {order_id}")
        complete_order = self.fetch_order_details(order_id)
        
        if complete_order:
            return complete_order
        else:
            return row


return_item = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("quantity", th.NumberType),
    th.Property("received_quantity", th.NumberType),
    th.Property("damaged_quantity", th.NumberType),
    th.Property("item_id", th.StringType),
    th.Property("return_id", th.StringType),
    th.Property("reason_id", th.StringType),
    th.Property("note", th.StringType),
    th.Property("metadata", th.CustomType({"type": ["object", "string"]})),
)

class ReturnsStream(MedusaStream):
    """Define custom stream."""

    name = "returns"
    path = "/returns"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.returns[*]"

    schema = th.PropertiesList(
        th.Property("items", th.ArrayType(return_item)),
        th.Property("id", th.StringType),
        th.Property("display_id", th.NumberType),
        th.Property("order_id", th.StringType),
        th.Property("status", th.StringType),
        th.Property("location_id", th.StringType),
        th.Property("exchange_id", th.StringType),
        th.Property("claim_id", th.StringType),
        th.Property("refund_amount", th.NumberType),
        th.Property("created_at", th.DateTimeType),
        th.Property("canceled_at", th.StringType),
        th.Property("received_at", th.StringType),
    ).to_dict()
