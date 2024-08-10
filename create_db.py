from website import app, db
from website.models import Contact

with app.app_context():
    db.create_all()


# Fill the 'Contact' Object in DB with the set default in config

    name = app.config['NAME']
    email = app.config['EMAIL']
    phone_number = app.config['PHONE_NUMBER']

    contact = Contact.query.first()
    if not contact:
        contact = Contact(name=name, email=email, phone=phone_number)
        db.session.add(contact)
        db.session.commit()
