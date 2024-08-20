import io
from flask import Blueprint, request, send_file, make_response, redirect, url_for
from website import db
from website.models import Image, Project, Contact

api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/createProject", methods=['POST'])
def createProject():
    name = request.form.get('project_name')
    description = request.form.get('project_description')
    picture_id = request.form.get('projcet_picture')

    if name and description and picture_id:
        project = Project(name = name, description = description, image = picture_id)
        db.session.add(project)
        db.session.commit()
    elif name and description:
        project = Project(name = name, description = description, image = 1)
        db.session.add(project)
        db.session.commit()

        message="The project '"+name+"' was created and added to the database"
        print("[API]: "+message)
        return message, 200
    elif not name:
        message="Error while creating a new project! No name recived"
        print("[API]: "+message)
        return message, 400
    else:
        message="Error while creating a new project! No description recived"
        print("[API]: "+message)
        return message, 400

@api_bp.route("/editContact", methods=['POST'])
def editContact():
    name = request.form.get('contact_name')
    email = request.form.get('contact_email')
    phone = request.form.get('contact_phone')

    contact = Contact.query.first()

    if contact:
        contact.name = name
        contact.email = email
        contact.phone = phone

        db.session.commit()

        message='Contact was successfully updated'
        print("[API]: "+message)
        return message, 200
    else:
        message='Contact table could not be found'
        print("[API]: "+message)
        return message, 404

@api_bp.route("/uploadImage", methods=['POST'])
def uploadImage():
    if 'image' not in request.files:
        message = "No file part in the request"
        print("[API]: "+message)
        return message, 400

    image_file = request.files['image']

    if image_file.filename == '':
        message = "No selected file"
        print("[API]: "+message)
        return message, 400

    mime_type = image_file.mimetype

    if not mime_type.startswith('image/'):
        message = "File is not an image"
        print("[API]: "+message)
        return message, 400

    image_data = image_file.read()

    new_image = Image(name=image_file.filename, data=image_data, mime_type=mime_type)

    db.session.add(new_image)
    db.session.commit()

    message = "An image was uploaded successfully"
    print("[API]: "+message)
    return message, 200

@api_bp.route("/getImage/<int:img_id>", methods=['GET'])
def getImage(img_id):
    if img_id is not None or img_id == 0:
        image = Image.query.get(img_id)
    else:
        image = Image.query.get(1)
    if image:
        extension = image.mime_type.split('/')[-1]
        filename = f"{image.name}.{extension}"
        print("MIME Type:", image.mime_type)
        response = make_response(send_file(
            io.BytesIO(image.data),
            mimetype=image.mime_type
        ))
        response.headers["Content-Disposition"] = f"inline; filename={filename}"
        return response
    else:
        return 'Image not found', 404

@api_bp.route("/deleteImage/<int:imageID>", methods=['POST'])
def deleteImage(imageID):
    image = Image.query.get(imageID)
    if image is not None:
        message = 'Image '+image.name+' has been deleted'
        db.session.delete(image)
        db.session.commit()
        print("[API]: "+message)
        return message, 200
    else:
        message = 'Image was not found'
        print("[API]: "+message)
        return message, 404

@api_bp.route("/deleteProject/<int:projectID>", methods=['POST']) # Add that it also deletes project-element orphans of project
def deleteProject(projectID):
    project = Project.query.get(projectID)
    if project is not None:
        message = 'Project '+project.name+' has been deleted'
        db.session.delete(project)
        db.session.commit()
        print("[API]: "+message)
        return message, 200
    else:
        message = 'Project was not found'
        print("[API]: "+message)
        return message, 404