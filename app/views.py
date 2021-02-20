from flask import render_template 
from app import app

#views 
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    message = 'Latest News'
    return render_template('index.html',message =  message)
    

@app.route('/')
def news():
    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html')

