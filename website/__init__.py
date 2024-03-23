from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#App inizialisierung
app = Flask(__name__)

#Rufe configuration auf
app.config.from_object('config')

#Datenbank initialisierung
db = SQLAlchemy()
db.init_app(app)

from website import routes