from flask import render_template
from website import app, db
from website.models import *

@app.route("/")
def landingPage():
    return render_template("index.html")

@app.route("/Projects")
def projectsPage():
    projects = db.session.execute(db.select(Project).order_by(Project.date)).scalars()
    return render_template("projects.html", projects)

@app.route("/Projects/<projectID>")
def projectPage(projectID):
    db.get_or_404(Project, projectID)
    return render_template("project.html", Project)

@app.route("/AboutMe")
def abouteMePage():
    return render_template("aboutMe.html")

@app.route("/Contact")
def contactPage():
    return render_template("contact.html")

@app.route("/Admin")
def adminPage():
    return render_template("adminIndex.html")