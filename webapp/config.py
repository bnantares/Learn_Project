from datetime import timedelta
import os

# абсолютный путь до этой папки
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

REMEMBER_COOKIE_DURATION = timedelta(days=10)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'fr$jhfhr$jvsjvnln@3km$kgmfs'
