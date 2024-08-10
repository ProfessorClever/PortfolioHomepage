from flask import render_template, request
from website import app, db
from website.models import *
from werkzeug.utils import secure_filename

#   --- User Sides ---

@app.route("/")
def landingPage():
    return render_template("index.html")

@app.route("/Projects")
def projectsPage():
    projects = db.session.execute(db.select(Project).order_by(Project.begin)).scalars()
    return render_template("projects.html", projects = projects)

@app.route("/Projects/<projectID>")
def projectPage(projectID):
    project = db.get_or_404(Project, int(projectID))
    return render_template("project.html", project = project)

@app.route("/AboutMe")
def abouteMePage():
    return render_template("aboutMe.html")

@app.route("/Contact")
def contactPage():
    contact = Contact.query.first_or_404()
    return render_template("contact.html", name = contact.name, email = contact.email, phone = contact.phone)

#   --- Admin Sides ---

@app.route("/Admin")
def adminPage():
    return render_template("adminIndex.html")

@app.route("/EditProjects")
def editProjectsPage():
    projects = db.session.execute(db.select(Project).order_by(Project.begin)).scalars()
    return render_template("editProjects.html", projects = None)

@app.route("/EditProjects/<projectID>")
def editProjectPage(projectID):
    project = db.get_or_404(Project, int(projectID))
    return render_template("editProject.html", project = project)

@app.route("/EditMe")
def editMePage():
    return render_template("editMe.html")

@app.route("/EditContact")
def editContactPage():
    contact = Contact.query.first()
    return render_template("editContact.html", name = contact.name, email = contact.email, phone = contact.phone)

#   --- DB Api ---

@app.route("/api/createProject", methods=['POST'])
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

@app.route("/api/editContact", methods=['POST'])
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

@app.errorhandler(404)
def notFoundPage(e):
    return render_template("404.html")