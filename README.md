# Project Name

News(News-API)
​
# Project Description

This is a application that helps users, especially those with very busy schedules, keep up with the news, by listing and previewing news articles from various sources.
​
# Author(s) Information

Rose Okoth.
​
# BDD

* Users should be able to:
    - see various news sources on the homepage of the application.
    - select a news source and see all news articles from the selected news source in the application.
    - see the image, description and the time a news article was created.
    - click on an article and read the full article on the source website.

# Setup Instructions

1. Clone the repo:
   * `git clone https://github.com/rose-okoth/News-API`
​
1. Switch into the directory:
   * `cd News-API`
​
# Running the application

1. Create the virtual environment
   * ` $ python3 -m venv --without-pip virtual `
   * ` $ source virtual/bin/env `
   * ` $ curl https://bootstrap.pypa.io/get-pip.py | python `

1. Installing Flask and other Modules
   * ` $ python3 -m pip install Flask`
   * ` $ python3 -m pip install Flask-Bootstrap`
   * ` $ python3 -m pip install flask-script`

1. Setting up the API Key

   To be able to gather article info from the News API you will need an API Key.

    * `Visit https://newsapi.org/ and register for an API key.`
    * `In the root directory of the project folder create a file: start.sh`
    * `Insert the following info into it:`

            export NEWS_API_KEY='<Your-Api-Key>'
            python3.6 manage.py server

    * `Insert the API Key you received from News Api where <Your-Api-Key> is.`

1. To run the application, in your terminal:
    *  `$ chmod +x start.sh`
    *  `$ ./start.sh`

# Testing the Application

1. To run the tests for the class files:
    * `$ python3 manage.py tests`
    
# Technologies Used

* Python3.
* Flask.
* HTML.
* Bootstrap.
​
# Contact Information

* Email: [Email](mailto:okoth.rose0@gmail.com)
* Phone number: [Phone](tel:+254712476547)
​
# License and Copyright Information
​
Copyright(c) 2021 - Rose Okoth.  
​
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
​
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
​
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
​
Reference: [MIT License](https://opensource.org/licenses/MIT)