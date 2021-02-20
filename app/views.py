from flask import render_template 
from app import app
from .request import get_news,process_results


#views 
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    all_news = get_news('everything')
    print(all_news)
    title = 'Welcome to the home of the Latest News'

    my_items = zip(source,author,title,description,url,publishedAt,urlToImage,anything)
    return render_template('index.html',title = title,everything = my_items)


@app.route('/news')
def news():
    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html')

