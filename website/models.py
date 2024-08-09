from website import db
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
import sqlalchemy as sa

metadata = sa.MetaData()
class Base(DeclarativeBase):
    pass

project_element = sa.Table(
    'project_element',
    metadata,
    sa.Column('project_id', sa.Integer, sa.ForeignKey('projects.id'), primary_key=True),
    sa.Column('element_id', sa.Integer, sa.ForeignKey('elements.id'), primary_key=True),
    sa.Column('prio', sa.Integer, nullable=False)
)

class Project(Base):
    __tablename__ = 'projects'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String, nullable=False)
    discription: Mapped[str] = mapped_column(sa.String, nullable=False)
    begin: Mapped[datetime] = mapped_column(datetime, default=sa.func.now(), nullable=False)
    elements: Mapped[list['Element']] = relationship(
        secondary='project_element',
        back_populates='projects',
        order_by='ProjectElement.prio'
    )

class Element(Base):
    __tablename__ = 'elements'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(sa.String, nullable=False)
    image_id: Mapped[int] = mapped_column(sa.ForeignKey('images.id'), nullable=True)
    html: Mapped[str] = mapped_column(nullable=True)
    projects: Mapped[list[Project]] = relationship(
        secondary='project_element',
        back_populates='elements'
    )

class Image(Base):
    __tablename__ = 'images'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key= True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String, nullable=False)
    data:Mapped[bytes] = mapped_column(sa.LargeBinary, nullable=False)
    mime_type: Mapped[str] = mapped_column(sa.String, nullable=False)