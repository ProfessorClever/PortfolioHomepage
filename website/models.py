from website import db
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa

class Image(db.Model):
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str]
    filename: Mapped[str] = mapped_column(nullable= False, unique= True)

class Text(db.Model):
    id: Mapped[int] = mapped_column(primary_key= True)
    text: Mapped[str]
    textType: Mapped[int] = mapped_column(nullable= False)
 
class Project(db.Model):
    id: Mapped[int] = mapped_column(primary_key= True)
    discription: Mapped[str]

project_element_m2m = db.Table(
    "project_element",
    sa.Column("project_id", sa.ForeignKey(Project.id), primary_key=True),
    sa.Column("element_id", primary_key=True),
)