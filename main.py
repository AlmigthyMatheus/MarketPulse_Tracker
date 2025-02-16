import time
import schedule
import logging
from api_integration.webscraper_api import get_web_scraper_data
from api_integration.aliexpress_api import get_aliexpress_product_description  # updated function
from api_integration.real_time_amazon_api import get_realtime_amazon_data
from data_processing.processor import process_data
from data_processing.storage import save_to_database
from utils.notifications import send_email_alert
from utils.logger import setup_logger

setup_logger()


def collect_and_process():
    logging.info("Starting data collection for MarketPulse Tracker...")

    # Retrieve data from the new AI Web Scraper API
    wikipedia_url = "https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue"
    web_data = get_web_scraper_data(wikipedia_url, summary=False)
    logging.info("Web Scraper data collected.")

    # Retrieve data from the new AliExpress API
    aliexpress_product_id = "1005006439167901"
    aliexpress_data = get_aliexpress_product_description(aliexpress_product_id)
    logging.info("AliExpress data collected.")

    # Retrieve data from Real Time Amazon Data API
    amazon_asin = "B07ZPKBL9V"
    amazon_data = get_realtime_amazon_data(amazon_asin, "US")
    logging.info("Real Time Amazon data collected.")

    # Process the collected data
    processed_df = process_data(web_data, aliexpress_data, amazon_data)
    logging.info("Data processed successfully.")

    # Save the processed data to the SQLite database
    save_to_database(processed_df)
    logging.info("Data saved to database.")

    # (Optional) Send an email alert with the processed data
    subject = "MarketPulse Tracker - Data Update"
    body = f"Updated data:\n\n{processed_df.to_string(index=False)}"
    # Uncomment the line below to enable email alerts:
    # send_email_alert(subject, body, "recipient@example.com")


def main():
    collect_and_process()
    schedule.every(30).minutes.do(collect_and_process)
    logging.info("Scheduler started: updating data every 30 minutes.")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
