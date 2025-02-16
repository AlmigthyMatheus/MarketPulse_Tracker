# api_integration/reviews_api.py
import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def get_product_reviews(product_id):
    """
    Consulta uma API de reviews para obter avaliações do produto.
    """
    url = "https://product-reviews.p.rapidapi.com/getReviews"
    querystring = {"productId": str(product_id)}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "product-reviews.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Erro ao coletar reviews: {e}")
        return {"error": str(e)}
