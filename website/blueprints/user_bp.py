from flask import Blueprint, render_template
from website import db
from website.models import Project, Contact

user_bp = Blueprint('user_bp', __name__, template_folder="templates")

@user_bp.route("/")
def landingPage():
    latestProject = Project.query.order_by(db.desc(Project.begin)).first()
    popularProject = Project.query.order_by(db.desc(Project.views)).first()

    if latestProject and popularProject:
        return render_template("index.html", latest = latestProject, popular = popularProject)
    elif not latestProject:
        return render_template("index.html", latest=None, popular = popularProject)
    elif not popularProject:
        return render_template("index.html", latest=latestProject, popularProject=None)
    else:
        return render_template("index.html", latest=None, popular=None)

@user_bp.route("/Projects")
def projectsPage():
    projects = db.session.execute(db.select(Project).order_by(Project.begin)).scalars()
    return render_template("projects.html", projects = projects)

@user_bp.route("/Projects/<projectID>")
def projectPage(projectID):
    project = db.get_or_404(Project, int(projectID))
    if project:
        project.views += 1
        db.session.commit()
    return render_template("project.html", project = project)

@user_bp.route("/AboutMe")
def abouteMePage():
    return render_template("aboutMe.html")

@user_bp.route("/Contact")
def contactPage():
    contact = Contact.query.first_or_404()
    return render_template("contact.html", name = contact.name, email = contact.email, phone = contact.phone)
