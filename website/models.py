from website import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    filename = db.Column(db.String, nullable=False, unique=True)

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    textType = db.Column(db.String)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    discription = db.Column(db.String)

class ProjectElement(db.Model):
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), primary_key=True)
    element_id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer)