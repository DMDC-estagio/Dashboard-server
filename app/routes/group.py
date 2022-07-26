from flask import Blueprint, render_template

groupRouter = Blueprint('group', __name__)

@groupRouter.route('/grupo')
def group():
    data = {'title': 'Grupo'}
    return render_template('./dashboard/group.html', data = data)