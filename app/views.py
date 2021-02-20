from flask import render_template 
from app import app
from .request import get_news, process_results
from config import news_api_base_url,api_key
import urllib.request,json
#views 
@app.route('/')
def index():
    get_news_url = news_api_base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None 
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    return news_results
def process_results(news_list):
    #Function that processes the news results
    source = []
    author = []
    title = []
    description = []
    url = []
    publishedAt = []
    urlToImage = []
    anything = []
    news_results = []
    for news_item in news_list:
        name = news_item.get('source')
        source.append(name.get('name'))
        author.append(news_item.get('author'))
        title.append(news_item.get('title'))
        description.append(news_item.get('description'))
        url.append(news_item.get('url'))
        publishedAt.append(news_item.get('publishedAt'))
        urlToImage.append(news_item.get('urlToImage'))
        anything.append('dsds')
    news_results=zip(source,author,title,description,url,publishedAt,urlToImage,anything)
    return render_template("index.html", content = news_results)