from flask import Blueprint, redirect, render_template, url_for
from website import db
from website.models import Project, Contact, Image, Tag

admin_bp = Blueprint('admin_bp', __name__, template_folder="templates")

@admin_bp.route("/")
def adminPage():
    return render_template("adminIndex.html")

@admin_bp.route("/EditProjects")
def editProjectsPage():
    projects = db.session.execute(db.select(Project).order_by(Project.begin)).scalars()
    return render_template("editProjects.html", projects = projects)

@admin_bp.route("/EditProjects/<projectID>")
def editProjectPage(projectID):
    project = db.get_or_404(Project, int(projectID))
    return render_template("editProject.html", project = project)

@admin_bp.route("/EditMe")
def editMePage():
    return render_template("editMe.html")

@admin_bp.route("/EditContact")
def editContactPage():
    contact = Contact.query.first()
    return render_template("editContact.html", name = contact.name, email = contact.email, phone = contact.phone)

@admin_bp.route("/ImageGallery")
def imageGallery():
    images = db.session.execute(db.select(Image).order_by(Image.id)).scalars()
    return render_template("imageGallery.html", images=images)

@admin_bp.route("/Tags")
def tags():
    tags = db.session.execute(db.select(Tag)).scalars()
    return render_template("tags.html", tags = tags)