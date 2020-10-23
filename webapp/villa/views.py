from flask import Blueprint, render_template

blueprint = Blueprint('/', __name__)


@blueprint.route("/")
def index():
    page_title = "Villas for Sale"
    return render_template('villa/index.html', page_title=page_title)
