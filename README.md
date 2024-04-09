# Amazon Reviews Scraper


This is a Flask web application that scrapes product reviews from Amazon. Users can search for a product on Amazon, open the product page, scroll down to view more reviews, and then copy the URL of the product page and paste it into the application. The application will then scrape the reviews from the provided URL and save them to a JSON file.

## Usage



1. Clone this repository to your local machine.
2. Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open your web browser and go to `http://localhost:5000`.
5. Enter the URL of the Amazon product page in the provided input field and click on the "Submit" button.
6. The application will scrape the reviews from the provided URL and save them to a JSON file named `amazon_reviews.json`.

## How to Use



1. Go to the [Amazon website](https://www.amazon.com) and search for the product whose reviews you want to scrape.
2. Click on the product to open its page.
3. Scroll down to view more reviews.
4. Click on the "See more reviews" button to load additional reviews.
5. Once you've loaded all the reviews you want to scrape, copy the URL of the product page.
6. Paste the copied URL into the input field on the Flask application and submit.
7. Wait for the scraping process to complete. Once completed, you'll see a message indicating that the process is finished.
8. You can find the scraped reviews in the `amazon_reviews.json` file in the same directory as the Flask application.




- This application relies on web scraping, which may violate the terms of service of some websites, including Amazon. Use it responsibly and ensure that you comply with the terms of service of the websites you scrape.
