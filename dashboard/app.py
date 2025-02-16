import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from api_integration.webscraper_api import get_web_scraper_data
from api_integration.aliexpress_api import get_aliexpress_product_description
from api_integration.real_time_amazon_api import get_realtime_amazon_data
from data_processing.processor import process_data
from data_processing.storage import save_to_database


def run_dashboard():
    st.title("MarketPulse Tracker Dashboard")

    st.sidebar.header("Settings")
    wikipedia_url = st.sidebar.text_input("Web Scraping URL",
                                          "https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue")
    aliexpress_product_id = st.sidebar.text_input("AliExpress Product ID", "1005006439167901")
    amazon_asin = st.sidebar.text_input("Amazon ASIN", "B07ZPKBL9V")

    if st.sidebar.button("Update Data"):
        with st.spinner("Fetching data..."):
            web_data = get_web_scraper_data(wikipedia_url, summary=False)
            aliexpress_data = get_aliexpress_product_description(aliexpress_product_id)
            amazon_data = get_realtime_amazon_data(amazon_asin, "US")
            processed_df = process_data(web_data, aliexpress_data, amazon_data)
            save_to_database(processed_df)

        st.success("Data updated!")

        with st.expander("Show Web Scraper JSON"):
            st.json(web_data)
        with st.expander("Show AliExpress JSON"):
            st.json(aliexpress_data)
        with st.expander("Show Amazon JSON"):
            st.json(amazon_data)

        st.subheader("Processed Data Table")
        st.dataframe(processed_df)

        # Show price comparison chart only if numeric Amazon Price is available.
        if processed_df["Amazon Price"].notnull().all():
            st.subheader("Price Comparison")
            chart_data = processed_df[["Amazon Price"]]
            st.bar_chart(chart_data)
        else:
            st.info("Price data is not available for charting.")
    else:
        st.info("Click 'Update Data' from the sidebar to fetch and display data.")


if __name__ == "__main__":
    run_dashboard()
