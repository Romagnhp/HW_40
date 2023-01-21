from sqlalchemy.orm import declarative_base
from sqlalchemy import TEXT, INTEGER, Column

ParentClass = declarative_base()

class MyColunms(ParentClass):
    __tablename__ = "people"

    id = Column(INTEGER, primary_key = True,  autoincrement = True)
    name = Column(TEXT)
    height = Column(INTEGER)
    eye_color = Column(TEXT)
    gender = Column(TEXT)

