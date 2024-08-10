from website import app, db
from website.models import Me

with app.app_context():
    db.create_all()


# Fill the 'Me' Object in DB with the set default in config

    name = app.config['NAME']
    email = app.config['EMAIL']
    phone_number = app.config['PHONE_NUMBER']

    me = Me.query.first()
    if not me:
        me = Me(name=name, email=email, phone=phone_number)
        db.session.add(me)
        db.session.commit()
