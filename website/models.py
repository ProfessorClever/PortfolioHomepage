from enum import Enum
from sqlalchemy import Table, Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from website import db

project_element = Table(
    'project_element',
    db.metadata,
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
    Column('element_id', Integer, ForeignKey('elements.id'), primary_key=True),
    Column('prio', Integer, nullable=False),
    UniqueConstraint('project_id', 'prio', name='uq_project_prio')
)

project_tag = Table(
    'project_tag',
    db.metadata,
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.Integer, db.ForeignKey('images.id'), nullable=False, default=1)
    description = db.Column(db.String, nullable=False)
    begin = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    views = db.Column(db.Integer, default=0)
    elements = relationship(
        'Element',
        secondary=project_element,
        back_populates='projects',
        order_by=project_element.c.prio
    )
    tags = relationship(
        'Tag',
        secondary=project_tag,
        back_populates='projects'
    )

class Element(db.Model):
    __tablename__ = 'elements'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    e_type = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String, nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'), nullable=True)
    html = db.Column(db.String, nullable=True)
    project_ref = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)
    link = db.Column(db.String, nullable=True)
    projects = relationship(
        'Project',
        secondary=project_element,
        back_populates='elements'
    )

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    icon = db.Column(db.String, db.ForeignKey('images.id'), nullable=False)
    projects = relationship(
        'Project',
        secondary=project_tag,
        back_populates='tags'
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

class ElementType(Enum):
    HTML = 1
    IMAGE = 2
    HEADER = 3
    LINK = 4
    PROJECT = 5
    TEXT = 6