from flask import Flask, render_template
import requests
import json
import pandas as pd
from decouple import config

app = Flask(__name__, template_folder = 'templates')

#API Credentials
API_KEY = config('API_KEY')
api_url = f"https://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key={ API_KEY }"

#Get API response
response = requests.get(api_url).json()

#set range of data
num_results = response["num_results"]
num_articles = [*range(0, num_results, 1)]

url = []
published_date = []
updated = []
section = []
byline = []
title = []
abstract = []
des_facet = []
org_facet = []
per_facet = []
geo_facet = []

#Parse api as dataframe
for x in num_articles:
    url1 = response['results'][x]['url']
    url.append(url1)

    published_date1 = response['results'][x]['published_date']
    published_date.append(published_date1)

    updated1 = response['results'][x]['updated']
    updated.append(updated1)

    section1 = response['results'][x]['section']
    section.append(section1)

    byline1 = response['results'][x]['byline']
    byline.append(byline1)

    title1 = response['results'][x]['title']
    title.append(title1)

    abstract1 = response['results'][x]['abstract']
    abstract.append(abstract1)

    des_facet1 = response['results'][x]['des_facet']
    des_facet.append(des_facet1)

    org_facet1 = response['results'][x]['org_facet']
    org_facet.append(org_facet1)

    per_facet1 = response['results'][x]['per_facet']
    per_facet.append(per_facet1)

    geo_facet1 = response['results'][x]['geo_facet']
    geo_facet.append(geo_facet1)

    nyt_data = pd.DataFrame({

        "url" : url,
        "published_date" : published_date,
        "updated" : updated,
        "section" : section,
        "byline" : byline,
        "title" : title,
        "abstract" : abstract,
        "des_facet" : des_facet,
        "org_facet" : org_facet,
        "per_facet" : per_facet,
        "geo_facet" : geo_facet
    })


@app.route('/')
def index():
    return render_template('index.html',
        url=url, 
        published_date=published_date,
        updated=updated,
        section=section,
        byline=byline,
        title=title,
        abstract = abstract,
        des_facet=des_facet,
        org_facet=org_facet,
        per_facet=per_facet,
        geo_facet=geo_facet    
        )