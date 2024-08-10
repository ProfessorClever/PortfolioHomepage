from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from website import db

project_element = Table(
    'project_element',
    db.metadata,
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
    Column('element_id', Integer, ForeignKey('elements.id'), primary_key=True),
    Column('prio', Integer, nullable=False)
)

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.Integer, db.ForeignKey('images.id'), nullable=True)
    description = db.Column(db.String, nullable=False)
    begin = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    elements = relationship(
        'Element',
        secondary=project_element,
        back_populates='projects',
        order_by=project_element.c.prio
    )

class Element(db.Model):
    __tablename__ = 'elements'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String, nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'), nullable=True)
    html = db.Column(db.String, nullable=True)
    projects = relationship(
        'Project',
        secondary=project_element,
        back_populates='elements'
    )

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)
    mime_type = db.Column(db.String, nullable=False)

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True, default=1)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
