import pandas as pd
import logging
import re


def extract_numeric_price(price_str):
    """
    Given a string like '$197.96', returns a float 197.96.
    If parsing fails, returns None.
    """
    if not price_str or not isinstance(price_str, str):
        return None
    numeric_part = re.sub(r"[^\d.]", "", price_str)
    try:
        return float(numeric_part)
    except ValueError:
        return None


def process_data(web_data, aliexpress_data, amazon_data=None):
    """
    Processes and combines data from multiple sources.

    - Title: Uses web_data["title"] if available; if not, uses amazon_data["product_title"].
    - AliExpress: Extracts description, image, media, stock, and quantity from the API response.
    - Amazon: Extracts the numeric price from amazon_data["product_price"].

    Returns a DataFrame with columns:
       Title, AliExpress Description, AliExpress Image, AliExpress Media,
       AliExpress Stock, AliExpress Quantity, Amazon Price.
    """
    try:
        # Title extraction
        title = web_data.get("title")
        if not title and amazon_data and "product_title" in amazon_data:
            title = amazon_data["product_title"]
        if not title:
            title = "No Title"

        # AliExpress data extraction:
        ali_response = aliexpress_data.get("response", {})
        ali_description = ali_response.get("description") or ali_response.get("result", "No Description")
        ali_image = ali_response.get("image", "No Image")
        ali_media = ali_response.get("media", [])
        ali_stock = ali_response.get("stock", "Not Available")
        ali_quantity = ali_response.get("quantity", "Not Available")

        # Amazon Price extraction
        amazon_price_str = None
        if amazon_data and "product_price" in amazon_data:
            amazon_price_str = amazon_data["product_price"]
        amazon_price = extract_numeric_price(amazon_price_str)

        df = pd.DataFrame({
            "Title": [title],
            "AliExpress Description": [ali_description],
            "AliExpress Image": [ali_image],
            "AliExpress Media": [ali_media],
            "AliExpress Stock": [ali_stock],
            "AliExpress Quantity": [ali_quantity],
            "Amazon Price": [amazon_price]
        })
        return df
    except Exception as e:
        logging.error(f"Error processing data: {e}")
        return pd.DataFrame()
