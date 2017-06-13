#initialize stuff 

from flask import Flask

app = Flask (__name__, instance_relative_config=True)


#Load views
from app import views


# load config file

app.config.from_object('config')
