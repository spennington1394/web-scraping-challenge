import os 
import pymongo
import pandas as pd 
import requests
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time 

def scrape():

    mars_dic = {}

    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)

    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('div',class_ = 'content_title').text
    para = soup.find('div',class_ = 'article_teaser_body').text

    mars_dic['Title'] = title
    mars_dic['Paragraph'] = para

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')

    image_url = soup.find("a",class_="button fancybox").get("data-fancybox-href")

    base_url = 'https://www.jpl.nasa.gov'

    featured_url = base_url + image_url

    mars_dic['Featured_URL'] = featured_url

    url3 = 'https://space-facts.com/mars/'

    time.sleep(1)

    tables = pd.read_html(url3)[0]

    table = df.to_html(classes = 'table')

    mars_dic['Table'] = table

    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)

    time.sleep(1) 

    hemispheres = []

    for i in range (4):
    
        browser.find_by_tag('h3')[i].click()
    
        html = browser.html
    
        soup = BeautifulSoup(html, 'html.parser')
    
        image = soup.find('img', class_='wide-image')['src']
    
        image_url = 'https://astrogeology.usgs.gov' + image
    
        title = soup.find('h2', class_= 'title').text 
    
        hemispheres.append({'Title': title, 'Image URL':image_url})
    
    
    mars_dic['Hemispheres'] = mars_hemispheres

    browser.quit()

    return mars_dic



