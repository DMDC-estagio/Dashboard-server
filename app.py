import random
import os
from datetime import datetime

from flask import Flask, Response, render_template, stream_with_context
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'
app. config["CACHE_TYPE"] = "null"

template_dir = os.path.abspath('./templates')
static_dir = os.path.abspath('./static')

db = SQLAlchemy(app)

random.seed()  # Initialize the random number generator

@app.route('/')
def index():
    return render_template('./dashboard/index.html', data = {'title': 'Início', 'teste': [{'time': datetime.fromtimestamp(953852555).strftime('%Y-%m-%d %H:%M:%S'), 'value': 20}, {'time': datetime.fromtimestamp(1816129816).strftime('%Y-%m-%d %H:%M:%S'), 'value': 12}, {'time': datetime.fromtimestamp(1200396315).strftime('%Y-%m-%d %H:%M:%S'), 'value': 13}, {'time': datetime.fromtimestamp(1180529430).strftime('%Y-%m-%d %H:%M:%S'), 'value': 14}, {'time': datetime.fromtimestamp(1252327542).strftime('%Y-%m-%d %H:%M:%S'), 'value': 17}]})
