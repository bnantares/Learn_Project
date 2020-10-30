from flask import Blueprint, render_template, redirect, url_for, flash
from webapp.object.forms import AddingLotForm
from webapp.db import db
from webapp.object.models import Object
from webapp.user.models import User

blueprint = Blueprint('lots', __name__, url_prefix='/lots')


@blueprint.route('/')
def lots():
    page_title = "Лоты на продажу"
    return render_template('object/lots.html', page_title=page_title)


@blueprint.route('/adding-lots')
def adding_lots():
    form = AddingLotForm()
    page_title = "Add lots"
    return render_template('object/adding_lots.html', page_title=page_title, form=form)


@blueprint.route('/process-add', methods=['POST'])
def process_add():
    form = AddingLotForm()
    if form.validate_on_submit():
        new_object = Object(description=form.description.data, starting_price=form.starting_price.data ,email=form.email.data, img=form.img.data)
        db.session.add(new_object)
        db.session.commit()
        flash('Вы успешно добавили лот')
        return redirect(url_for('/.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('lots.adding_lots'))
