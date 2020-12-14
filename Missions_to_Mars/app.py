from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

connect = PyMongo(app, uri='mongodb://localhost:27017/mars_app')

@app.route('/')
def home():

    scraped = connect.db.collection.find_one()

    return render_template('index.html', scraped=scraped)

@app.route('/scrape')
def scrape():

    scraped = scrape_mars.scrape()

    connect.db.collection.update({}, scraped, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)