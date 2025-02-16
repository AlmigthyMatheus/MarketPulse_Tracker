import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


def get_realtime_amazon_data(asin, country="US"):
    """
    Retrieves product details from the Real Time Amazon Data API.

    :param asin: The ASIN of the Amazon product.
    :param country: The country code (default "US").
    :return: The product details as a JSON object.
    """
    url = "https://real-time-amazon-data.p.rapidapi.com/product-details"
    querystring = {"asin": asin, "country": country}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error retrieving data from Real Time Amazon Data API: {e}")
        return {"error": str(e)}
