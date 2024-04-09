
from flask import Flask,render_template,request
import requests
import logging
import os
from bs4 import BeautifulSoup
import json
logging.basicConfig(filename="scrapper.log" , level=logging.INFO)
app = Flask(__name__)


@app.route("/" , methods = ["GET"])

def home():
    return render_template("index.html")

@app.route("/review",  methods = ["POST" , "GET"])

def index():
    if request.method == 'POST': 
        try:
            url = request.form["content"]
         



            headers = {
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            reviews = soup.find_all("div", {"data-hook": "review"})

           # Create a list to store data
            data = []

            for review in reviews:
                reviewer = review.find("span", class_="a-profile-name").text.strip()
                rating = review.find("i", class_="review-rating").text.strip()
                date = review.find("span", class_="a-size-base a-color-secondary review-date").text.strip()
                title = review.find("a", class_="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold").text.strip()
                body = review.find("span", class_="a-size-base review-text review-text-content").text.strip()
    
                   # Append data to the list as a dictionary
                data.append({
                 "Reviewer": reviewer,
                 "Rating": rating,
                 "Date": date,
                 "Title": title,
                 "Body": body
                        })

               # Save data to a JSON file
                with open('amazon_reviews.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
        except Exception as e:
            logging.info(e)
            return 'something is wrong' 
                
        return 'data is completed in your folder'
    
    else:
       return render_template('index.html')       
                
                
    
    
if __name__ == "__main__":
    app.run(debug=True)
