# api_integration/affiliate_api.py
import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def get_amazon_product_detail(product_id):
    """
    Consulta a API de produtos da Amazon para obter detalhes.
    """
    url = "https://amazon-product-price-tracker.p.rapidapi.com/products/detail"
    querystring = {"productId": str(product_id)}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "amazon-product-price-tracker.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Erro ao coletar dados do Amazon: {e}")
        return {"error": str(e)}
