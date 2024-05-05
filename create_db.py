from website import app, db
from website import models

with app.app_context():
    db.create_all()