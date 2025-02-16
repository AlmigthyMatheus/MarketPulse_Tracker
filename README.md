# MarketPulse Tracker 🚀

MarketPulse Tracker is an interactive dashboard that aggregates real-time market data from multiple APIs, including a web scraper, AliExpress, and Amazon. The premium version provides exclusive insights for just $5. 💰

## Features ✨

- **Real-Time Data Integration:** Collects data from multiple APIs.
- **Interactive Dashboard:** Built with Streamlit for dynamic interaction.
- **Data Processing:** Cleans and combines data from different sources.
- **Access Control & Payment Integration:** Premium access available for $5.
- **Future Enhancements:** Options for data export, custom analytics, and subscription-based updates.

## Installation ⚙️

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file (refer to `.env.example`) with your credentials:

   ```ini
   RAPIDAPI_KEY=your_rapidapi_key_here
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your_email@gmail.com
   SMTP_PASSWORD=your_app_password
   ```

## Running the Project ▶️

- **Data Collection:**  
  Run the main process with:

  ```bash
  python main.py
  ```

- **Interactive Dashboard:**  
  Launch the dashboard with:

  ```bash
  streamlit run dashboard/app.py
  ```

## Demo Results and Explanation 🔍

### A. Web Scraper

- **Tested Website:**  
  [Wikipedia: List of Largest Technology Companies by Revenue](https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue)
- **Sample Result Image:**  
  ![Web Scraper Result](images/web-scraper.png)

**Explanation:**  
The web scraper gathers data from the provided URL (Wikipedia in this case) and extracts key information. The raw JSON data is available for inspection in the dashboard. 📊

### B. AliExpress

- **Tested Product:**  
  [AliExpress Product](https://www.aliexpress.com/item/1005006439167901.html)
- **Sample Result Image:**  
  ![AliExpress Product Result](images/aliexpress.png)

**Explanation:**  
The AliExpress API returns product details such as description, image, media, stock, and quantity. (Note: The endpoint does not return price.) 🛒

### C. Amazon

- **Tested Product (Amazon):**  
  [Amazon Product Page (Example)](https://www.amazon.com/dp/B07ZPKBL9V)
- **Sample Result Image:**  
  ![Amazon Product Result](images/amazon.png)

**Explanation:**  
The Amazon API extracts product details including price. The price is processed to remove currency symbols and is used in the price comparison chart. 💵

## Service Offering on Freelance Platforms 💼

I offer a complete solution to develop and deploy an interactive MarketPulse Tracker Dashboard with real-time data integration using Python and RapidAPI. This service includes custom dashboard development, API integration, data processing, and premium access integration.

## License 📄

MIT License
