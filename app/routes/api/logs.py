import json
from os import remove
from flask import Blueprint
from pytz import timezone
from app.models.measure import Measure
from app.helpers.paginate import paginate

logsApiRouter = Blueprint('apiLogs', __name__)

@logsApiRouter.route('/logs', methods=['GET'])
def logs():
    query = Measure.query.order_by(Measure.date.desc())
    paginated = paginate(query, per_page = 15)

    response = [x.__dict__ for x in paginated['items']]
    for item in response:
        del item['_sa_instance_state']
        item['date'] = item['date'].replace(tzinfo=timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S')

    data = {'page': paginated['page'], 'total_pages': paginated['total_pages'], 'items_per_page': len(response), 'logs': response}

    return json.dumps(data), 200

def change_timezone(measure_list):
    for measure in measure_list:
        measure['date'] = measure['date'].replace(tzinfo=timezone('America/Sao_Paulo'))
    return measure_list