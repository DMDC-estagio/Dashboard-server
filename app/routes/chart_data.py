from flask import Blueprint, render_template, request, jsonify
from app import db
from app.models.measure import Measure

from pytz import timezone
from datetime import datetime

chartRouter = Blueprint('chartData', __name__)

@chartRouter.route('/chart_data/', methods=['POST'])
def chart_data():
    body = dict(request.get_json())
    try:
        verifyParams(body)

        new_mesure = Measure(date=datetime.now(timezone('America/Sao_Paulo')),voltageMed=body['voltage']['med'], currentMed=body['current']['med'], voltageMAx=body['voltage']['max'], currentMAx=body['current']['max'], voltageMin=body['voltage']['min'], currentMin=body['current']['min'])

        db.session.add(new_mesure)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'Status': 'BAD REQUEST','error': str(e)}), 400

    return jsonify({'Status': 'OK', 'Status': 'Measurement created with sucessfull'}), 201

def verifyParams(body):
    if 'voltage' not in body or 'current' not in body:
        raise Exception('Missing parameters voltage or current in body')
    if 'med' not in body['voltage'] or 'max' not in body['voltage'] or 'min' not in body['voltage']:
        raise Exception('Missing voltage parameters in body')
    if 'med' not in body['current'] or 'max' not in body['current'] or 'min' not in body['current']:
        raise Exception('Missing current parameters in body')
    if (type(body['voltage']['med']) != float and type(body['voltage']['med']) != int) or (type(body['voltage']['max']) != float and type(body['voltage']['max']) != int) or (type(body['voltage']['min']) != float and type(body['voltage']['min']) != int):
        raise Exception('Invalid type of parameters in body, need float or int')
    return True