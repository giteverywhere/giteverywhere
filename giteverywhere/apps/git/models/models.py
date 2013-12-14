from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    ForeignKey
    )

from . import DBSession, Base

#class MyModel(Base):
#    __tablename__ = 'repo_names'
#   id = Column(Integer, primary_key=True)
#    name = Column(Unicode(200), unique=True)

#    def __init__(self, title, content):
#        self.title = title


class Repository(Base):
    __tablename__ = 'repositories'
    #__table_args__ = {'extend_existing': True}

    repo_id = Column(Unicode(100), primary_key=True)
    repo_name = Column(Unicode(200), unique=True) 
    repo_path = Column(Unicode(200), unique=True)
    description = Column(UnicodeText)

    def __json__(self, request):
        return dict(repo_id=self.repo_id, repo_name=self.repo_name,
                    repo_path=self.repo_path, description=self.description)
