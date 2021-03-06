from flask import render_template,request
from . import main
from ..request import get_news, process_results
from config import news_api_base_url,api_key,sources_base_url
import urllib.request,json
# from ..models import Review

#views 
@main.route('/')
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

    # image_repo = ['https://media.istockphoto.com/photos/nairobi-cityscape-capital-city-of-kenya-picture-id637912692?k=6&m=637912692&s=612x612&w=0&h=dmUFmQbZfY6HpoZOiGUtMOv6W0COMp_ykIKxZdWhX0g=','https://www.gettyimages.com/gi-resources/images/500px/983794168.jpg','https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg',]
    
    for news_item in news_list:
        name = news_item.get('source')
        source.append(name.get('name'))
        author.append(news_item.get('author'))
        title.append(news_item.get('title'))
        description.append(news_item.get('description'))
        url.append(news_item.get('url'))
        publishedAt.append(news_item.get('publishedAt'))
        urlToImage.append(news_item.get('urlToImage'))
        anything.append('')

        # image = news_item['urlToImage']
        # if not image == None:
        #     image.append(image)
        # else:
        #     image.append(random.choice(image_repo))

    news_results=zip(source,author,title,description,url,publishedAt,urlToImage,anything)
    return render_template("index.html", content = news_results)


# @app.route('/news/')
# def news(news):
#     get_sources_url = sources_base_url.format(api_key)
#     with urllib.request.urlopen(get_sources_url) as url:
#         get_sources_data = url.read()
#         get_sources_response = json.loads(get_sources_data)
#         sources_results = None 
#         if get_sources_response['sources']:
#             sources_results_list = get_sources_response['sources']
#             sources_results = process_results(sources_results_list)
#     return sources_results
# def process_results(sources_list):
#     #Function that processes the news results
#     name = []
#     description = []
#     url = []
#     category = []
#     country= []
#     anything = []
#     sources_results = []
#     for sources_item in sources_list:
#         name.append(sources_item.get('name'))
#         description.append(sources_item.get('description'))
#         url.append(sources_item.get('url'))
#         category.append(sources_item.get('category'))
#         country.append(sources_item.get('country'))
#         anything.append('dsds')
#     sources_results=zip(name,description,url,category,country,anything)
#     return render_template("news.html", sources = sources_results)