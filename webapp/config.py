import os

basedir = os.path.abspath(os.path.dirname(__file__)) #абсолютный путь до этой папки

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
#print(SQLALCHEMY_DATABASE_URI)