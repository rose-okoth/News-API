from flask import Flask 
from .config import DevConfig

#initializing app
app = Flask(__name__)

#config setup
app.config.from_object(DevConfig)


from app import views 