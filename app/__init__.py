import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config["CACHE_TYPE"] = "null"

template_dir = os.path.abspath('./templates')
static_dir = os.path.abspath('./static')

db = SQLAlchemy(app)


