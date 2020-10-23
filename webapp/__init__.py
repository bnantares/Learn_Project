from flask_login import LoginManager
from flask_migrate import Migrate
from flask import Flask

from webapp.db import db
from webapp.villa.views import blueprint as villa_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.object.views import blueprint as object_blueprint

from webapp.image.models import Image
from webapp.object.models import Object
from webapp.user.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(villa_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(object_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
