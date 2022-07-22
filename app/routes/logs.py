from flask import Blueprint, render_template
from pytz import timezone
from app.models.measure import Measure

logsRouter = Blueprint('logs', __name__)

@logsRouter.route('/logs')
def logs():
    measure_list = Measure.query.all()
    response = [x.__dict__ for x in measure_list]
    try: response.sort(key=lambda x: x['date'].timestamp(), reverse=True)
    except: pass
    for item in response: item['date'] = item['date'].replace(tzinfo=timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('./dashboard/logs.html', data = {'title': 'Logs', 'logs': response})
