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
    project = db.get_or_404(Project, projectID)
    return render_template("project.html", project = project)

@app.route("/AboutMe")
def abouteMePage():
    return render_template("aboutMe.html")

@app.route("/Contact")
def contactPage():
    return render_template("contact.html")

#   --- Admin Sides ---

@app.route("/Admin")
def adminPage():
    return render_template("adminIndex.html")

@app.route("/EditProjects")
def editProjectsPage():
    return render_template("editProjects.html")

@app.route("/EditProjects/<projectID>")
def editProjectPage(projectID):
    project = db.get_or_404(Project, projectID)
    return render_template("editProject.html", project = project)

@app.route("/EditMe")
def editMePage():
    return render_template("editMe.html")

@app.route("/EditContact")
def editContactPage():
    return render_template("editContact.html")

#   --- DB Api ---

@app.route("/api/createProject", methods=['POST'])
def createProject():
    name = request.form.get('project_name')
    description = request.form.get('project_description')
    picture_id = request.form.get('projcet_picture')

    print(description)

    if name and description:
        project = Project(name = name, description = description, image = picture_id)
        db.session.add(project)
        db.session.commit()
        print("[API]: The project '"+name+"' was created and added to the database")
        return 'Project has been created', 200
    elif not name:
        print("[API]: Error while creating a new project")
        return 'No name recived', 400
    else:
        print("[API]: Error while creating a new project")
        return 'No Discription recived', 400



@app.errorhandler(404)
def notFoundPage(e):
    return render_template("404.html")