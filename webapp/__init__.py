from flask import Flask, render_template, url_for, request
from webapp.model import db, Users, Objects



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    @app.route('/index')
    @app.route('/')
    def index():
        return render_template('index.html', title='Villas')

    @app.route('/registration')
    def registration():
        return render_template('registration.html', title='Registration')
    return app



#if __name__ == '__main__':
#    app.run(debug=True)