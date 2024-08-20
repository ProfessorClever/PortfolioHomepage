import io
from flask import Blueprint, request, send_file, redirect, url_for
from website import db
from website.models import Image, Project, Contact

api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/createProject", methods=['POST'])
def createProject():
    name = request.form.get('project_name')
    description = request.form.get('project_description')
    picture_id = request.form.get('projcet_picture')

    if name and description:
        project = Project(name = name, description = description, image = picture_id)
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
    
@api_bp.route("/getImage/<int:img_id>", methods=['GET'])
def getImage(img_id):
    if img_id is not None:
        image = Image.query.get(img_id)
    else:
        image = Image.query.get(1)
    if image:
        return send_file(
            io.BytesIO(image.data),
            mimetype=image.mime_type,
            as_attachment=True,
            download_name=image.name
        )
    else:
        return 'Image not found', 404

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