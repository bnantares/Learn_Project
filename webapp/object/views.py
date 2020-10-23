from flask import Blueprint, render_template

blueprint = Blueprint('lots', __name__, url_prefix='/lots')


@blueprint.route('/')
def lots():
    page_title = "Лоты на продажу"
    return render_template('object/lots.html', page_title=page_title)
