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

    response = serializeData([x.__dict__ for x in paginated['items']])
    # for item in response: del item['_sa_instance_state']
    print(response)
    data = {'page': paginated['page'], 'total_pages': paginated['total_pages'], 'total_items': len(response), 'logs': response}

    return json.dumps(data), 200

def serializeData(measure_list):
    for measure in measure_list:
        measure_list[measure_list.index(measure)] = {
            'id': measure['id'],
            'voltage': {
                'max': measure['voltageMAx'],
                'med': measure['voltageMed'],
                'min': measure['voltageMin']
            },
            'current': {
                'max': measure['currentMAx'],
                'med': measure['currentMed'],
                'min': measure['currentMin']
            },
            'date': measure['date'].strftime('%Y-%m-%d %H:%M:%S')
        }
    return measure_list