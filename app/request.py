# from app import app
import urllib.request,json
from .models import News
# from .models import news
from instance.config import news_api_base_url,api_key
from flask import render_template 

# News = news.News

# #api key
# api_key = app.config['api_key']

# #news base url
# base_url = app.config['news_api_base_url']

# def configure_request(app):
#     global api_key,base_url
#     news_api_base_url = app.config['https://newsapi.org/v2/top-headlines?q=all&apiKey=8c39155e2f654098827b9fc8512d091b']  
#     api_key = app.config['8c39155e2f654098827b9fc8512d091b'] 


def get_news(everything):
    '''
    Function that gets the response to our request
    '''
    get_news_url = news_api_base_url.format(everything,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None 

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''
    Function that processes the news results
    '''
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

        source.append(news_item.get('source'))
        author.append(news_item.get('author'))
        title.append(news_item.get('title'))
        description.append(news_item.get('description'))
        url.append(news_item.get('url'))
        publishedAt.append(news_item.get('publishedAt'))
        urlToImage.append(news_item.get('urlToImage'))
        anything.append('')

    news_results=zip(source,author,title,description,url,publishedAt,urlToImage,anything)
    return news_results