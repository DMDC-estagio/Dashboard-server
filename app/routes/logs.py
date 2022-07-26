from flask import Blueprint, render_template, request
from pytz import timezone
from app.models.measure import Measure

logsRouter = Blueprint('logs', __name__)

@logsRouter.route('/logs')
def logs():
    page = request.args.get('page', default = 1, type = int)
    total_pages = Measure.query.count()//15
    total_pages += 1 if Measure.query.count()%15 != 0 else 0
    measure_list = Measure.query.order_by(Measure.date.desc()).paginate(page=page, per_page=15).items
    response = [x.__dict__ for x in measure_list]
    try: response.sort(key=lambda x: x['date'].timestamp(), reverse=True)
    except: pass
    for item in response: item['date'] = item['date'].replace(tzinfo=timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('./dashboard/logs.html', data = {'title': 'Logs', 'logs': response, 'page': page, 'total_pages': total_pages, 'items_per_page': len(response)})
