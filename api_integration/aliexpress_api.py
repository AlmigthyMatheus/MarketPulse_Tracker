import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


def get_aliexpress_product_description(product_id):
    """
    Retrieves product information (description, image, media, stock, quantity)
    from the new AliExpress API.

    :param product_id: The product's ID.
    :return: The product data as a JSON object.
    """
    url = "https://aliexpress-data.p.rapidapi.com/product/description-light"
    querystring = {"productId": str(product_id)}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "aliexpress-data.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error retrieving data from new AliExpress API: {e}")
        return {"error": str(e)}
