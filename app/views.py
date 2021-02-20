from flask import render_template 
from app import app

#views 
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Welcome to the home of the Latest News'
    return render_template('index.html',title =  title)


@app.route('/news')
def news():
    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html')

