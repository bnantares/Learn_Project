from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField
from webapp.object.models import Object


class AddingLotForm(FlaskForm):
    description = StringField('Описание', render_kw={"textarea class": "form-control"})
    img = FileField('Фото', render_kw={"class": "form-control-file"})
    starting_price = StringField('Цена', render_kw={"class": "form-control"})
    email = StringField('Электронная почта', render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-success"})
