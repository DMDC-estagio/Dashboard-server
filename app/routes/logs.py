from flask import Blueprint, render_template, request
from pytz import timezone
from app.models.measure import Measure
from app.helpers.paginate import paginate

logsRouter = Blueprint('logs', __name__)

@logsRouter.route('/logs')
def logs():
    query = Measure.query.order_by(Measure.date.desc())
    paginated = paginate(query, per_page = 15)

    response = [x.__dict__ for x in paginated['items']]
    for item in response: item['date'] = item['date'].replace(tzinfo=timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S')

    data = {'title': 'Logs', 'logs': response, 'page': paginated['page'], 'total_pages': paginated['total_pages'], 'items_per_page': len(response)}

    return render_template('./dashboard/logs.html', data = data )

def change_timezone(measure_list):
    for measure in measure_list:
        measure['date'] = measure['date'].replace(tzinfo=timezone('America/Sao_Paulo'))
    return measure_list