from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # Initialize app

app.config.from_object('config') # Assign config file

db = SQLAlchemy() # Initialize database
db.init_app(app)

from website import models

from website.blueprints.user_bp import user_bp
from website.blueprints.admin_bp import admin_bp
from website.blueprints.api_bp import api_bp

app.register_blueprint(user_bp) # Register the blueprints containing the routes
app.register_blueprint(admin_bp, url_prefix="/Admin")
app.register_blueprint(api_bp, url_prefix="/Api")

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404
