from flask import render_template
from website import app

@app.route("/")
def landingPage():
    return render_template("index.html")

@app.route("/Projects")
def projectsPage():
    return render_template("projects.html")

@app.route("/Projects/<projectID>")
def projectPage(projectID):
    return render_template("project.html", projectID = projectID)

@app.route("/AboutMe")
def abouteMePage():
    return render_template("aboutMe.html")

@app.route("/Contact")
def contactPage():
    return render_template("contact.html")