from flask import Blueprint, render_template

groupRouter = Blueprint('group', __name__)

@groupRouter.route('/grupo')
def group():
    return render_template('./dashboard/group.html', data = {'title': 'Grupo'})