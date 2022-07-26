from flask import Blueprint, render_template
from pytz import timezone
from app.models.measure import Measure

indexRouter = Blueprint('index', __name__)

@indexRouter.route('/')
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
    try:
        med_voltage /= len(measure_list)
        med_current /= len(measure_list)
    except:
        med_voltage = 0
        med_current = 0

    data = {'title': 'Início', 'tensao': response, 'tensao_max': f"{round(max_voltage,1)}".split('.'), 'corrente_max': f"{round(max_current,1)}".split('.'), 'tensao_med' : f"{round(med_voltage,1)}".split("."), "corrente_med" : f"{round(med_current,1)}".split(".")}

    return render_template('./dashboard/index.html', data = data)
