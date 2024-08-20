from website import app, db
from website.models import Contact, Image
import os

with app.app_context():
    db.create_all()

    name = app.config['NAME']
    email = app.config['EMAIL']
    phone_number = app.config['PHONE_NUMBER']
    default_image_path = app.config['DEFAULT_IMAGE_PATH']

    contact = Contact.query.first()
    if not contact: # Fill the 'Contact' Object in DB with the set default in config
        contact = Contact(name=name, email=email, phone=phone_number)
        db.session.add(contact)
        db.session.commit()

    image = Image.query.get(1)
    if not image: # Add the default Picture into DB
        try:
            with open(default_image_path, 'rb') as file:
                image_data = file.read()
            datatype = os.path.splitext(default_image_path)[1][1:]
            if datatype == "svg": datatype = datatype+"xml"
            mime_type = "image/"+datatype

            image = Image(id=1, name="default_image", data=image_data, mime_type='image/svg+xml')
            db.session.add(image)
            db.session.commit()
            print("Default image has been added to the database.")
        except FileNotFoundError:
            print(f"Error: Default image file not found at path: {default_image_path}")