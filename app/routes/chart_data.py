from flask import Blueprint, render_template, request, jsonify
from app import timezone, datetime, db
from app.models.measure import Measure

chartRouter = Blueprint('chartData', __name__)

@chartRouter.route('/chart_data/', methods=['POST'])
def chart_data():
    body = dict(request.get_json())
    try:
        new_mesure = Measure(date=datetime.now(timezone('America/Sao_Paulo')),voltageMed=body['voltage']['med'], currentMed=body['current']['med'], voltageMAx=body['voltage']['max'], currentMAx=body['current']['max'], voltageMin=body['voltage']['min'], currentMin=body['current']['min'])
        db.session.add(new_mesure)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'Status': 'Maybe something is missing','error': str(e)}), 500
    return jsonify({'success': 'ok'}), 201