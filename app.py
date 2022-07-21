import random
import os
from datetime import datetime
from pytz import timezone

from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'
app.config["CACHE_TYPE"] = "null"

template_dir = os.path.abspath('./templates')
static_dir = os.path.abspath('./static')

db = SQLAlchemy(app)

class Measure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    voltageMed = db.Column(db.Float)
    currentMed = db.Column(db.Float)
    voltageMAx = db.Column(db.Float)
    currentMAx = db.Column(db.Float)
    voltageMin = db.Column(db.Float)
    currentMin = db.Column(db.Float)

random.seed()  # Initialize the random number generator

@app.route('/')
def index():
    measure_list = Measure.query.all()
    response = []
    max_voltage, max_current = 0, 0
    med_voltage, med_current = 0, 0
    for item in measure_list:
        response.append({'time': item.date.replace(tzinfo=timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S'), 'med': item.voltageMed, 'min': item.voltageMin, 'max': item.voltageMAx})
        if item.voltageMAx > max_voltage:
            max_voltage = item.voltageMAx
        if max_current < item.currentMAx:
            max_current = item.currentMAx
        med_voltage += item.voltageMed
        med_current += item.currentMed
        # print(item.date.replace(tzinfo=timezone('America/Sao_Paulo')), item.date)
    med_voltage /= len(measure_list)
    med_current /= len(measure_list)

    return render_template('./dashboard/index.html', data = {'title': 'Início', 'tensao': response, 'tensao_max': f"{round(max_voltage,1)}".split('.'), 'corrente_max': f"{round(max_current,1)}".split('.'), 'tensao_med' : f"{round(med_voltage,1)}".split("."), "corrente_med" : f"{round(med_current,1)}".split(".")})

@app.route('/logs')
def logs():
    measure_list = Measure.query.all()
    response = [x.__dict__ for x in measure_list]
    for item in response: item['date'] = item['date'].replace(tzinfo=timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('./dashboard/logs.html', data = {'title': 'Logs', 'logs': response})

@app.route('/grupo')
def group():
    return render_template('./dashboard/group.html', data = {'title': 'Grupo'})

@app.route('/chart_data/', methods=['POST'])
def chart_data():
    new_mesure = Measure(voltageMed=random.randint(0, 100), currentMed=random.randint(0, 100), voltageMAx=random.randint(0, 100), currentMAx=random.randint(0, 100), voltageMin=random.randint(0, 100), currentMin=random.randint(0, 100))
    db.session.add(new_mesure)
    db.session.commit()
    return jsonify(request.get_json())

@app.route('/chart_data/voltage')
def chart_data_voltage():
    measure_list = Measure.query.all()
    response = []
    for item in measure_list:
        response.append({'time': item.date.strftime('%Y-%m-%d %H:%M:%S'), 'med': item.voltageMed, 'min': item.voltageMin, 'max': item.voltageMAx})

    return jsonify(response)

@app.route('/chart_data/amperage')
def chart_data_amperage():
    measure_list = Measure.query.all()
    response = []
    for item in measure_list:
        response.append({'time': item.date.strftime('%Y-%m-%d %H:%M:%S'), 'med': item.currentMed, 'min': item.currentMin, 'max': item.currentMAx})

    return jsonify(response)