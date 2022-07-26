from flask import Blueprint, render_template
from pytz import timezone
from app.models.measure import Measure

indexRouter = Blueprint('index', __name__)

@indexRouter.route('/')
def index():
    measure_list = [x.__dict__ for x in Measure.query.order_by(Measure.date.asc()).limit(15)]
    max_voltage, max_current = getMax(measure_list, 'voltageMAx'), getMax(measure_list, 'currentMAx')
    med_voltage, med_current = getMean(measure_list, 'voltageMed'), getMean(measure_list, 'currentMed')

    response = [{
        'time': x['date'].replace(tzinfo=timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S'),
        'med': x['voltageMed'],
        'min': x['voltageMin'],
        'max': x['voltageMAx']
    } for x in measure_list]

    data = {
        'title': 'Início',
        'tensao': response,
        'tensao_max': f'{round(max_voltage,1)}'.split('.'),
        'corrente_max': f'{round(max_current,1)}'.split('.'),
        'tensao_med' : f'{round(med_voltage,1)}'.split('.'),
        'corrente_med' : f'{round(med_current,1)}'.split('.')
    }

    return render_template('./dashboard/index.html', data = data)


def getMax(list, key):
    return max(list, key=lambda x: x['voltageMAx'])[key]

def getMean(list, key):
    return sum([x[key] for x in list]) / len(list)