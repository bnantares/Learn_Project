from flask import Flask, render_template, url_for, request
from webapp.model import db, Users, Objects



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    @app.route('/index')
    @app.route('/')
    def index():
        return render_template('index.html', title='Real Estate Selling project by M.Knyazev & A.Petrov')

    @app.route('/registration')
    def registration():
        return render_template('registration.html', title='Registration')
    return app

#Test
#set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
#if __name__ == '__main__':
#    app.run(debug=True)