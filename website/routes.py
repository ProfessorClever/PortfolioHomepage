from flask import render_template
from website import app, db
from website.models import *

@app.route("/")
def landingPage():
    return render_template("index.html")

@app.route("/Projects")
def projectsPage():
    projects = db.session.execute(db.select(Project).order_by(Project.date)).scalars()
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

@app.route("/Admin")
def adminPage():
    return render_template("adminIndex.html")

@app.route("/editProjects")
def editProjectsPage():
    return render_template("editProjects.html")

@app.route("/editProjects/<projectID>")
def editProjectPage(projectID):
    project = db.get_or_404(Project, projectID)
    return render_template("editProject.html", project = project)

@app.route("/editMe")
def editMePage():
    return render_template("editMe.html")

@app.route("/editContact")
def editContactPage():
    return render_template("editContact.html")

@app.errorhandler(404)
def notFoundPage(e):
    return render_template("404.html")