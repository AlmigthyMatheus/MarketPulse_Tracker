import os
import requests
import logging
import time
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


def get_web_scraper_data(url_to_scrape, summary=True, retries=3, delay=5):
    """
    Retrieves data from the new AI Web Scraper API.

    :param url_to_scrape: URL of the page to scrape.
    :param summary: Boolean flag to indicate if a summary is needed.
    :param retries: Number of retries on 429 errors.
    :param delay: Delay in seconds between retries.
    :return: The scraped data as a JSON object.
    """
    api_url = "https://ai-web-scraper1.p.rapidapi.com/"
    payload = {
        "url": url_to_scrape,
        "summary": summary
    }
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "ai-web-scraper1.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    attempt = 0
    while attempt < retries:
        try:
            response = requests.post(api_url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            if response.status_code == 429:
                logging.warning(
                    f"429 Too Many Requests. Retrying in {delay} seconds... (Attempt {attempt + 1}/{retries})")
                time.sleep(delay)
                attempt += 1
            else:
                logging.error(f"Error retrieving data from AI Web Scraper API: {e}")
                return {"error": str(e)}
    return {"error": "Max retries reached. Too many requests."}
