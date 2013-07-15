from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    ForeignKey
    )

from . import DBSession, Base


# Create your models here. 
  
class Repository(Base):
    __tablename__ = 'repositories'
    #__table_args__ = {'extend_existing': True}

    repo_id = Column(Unicode(100), primary_key=True)
    repo_name = Column(Unicode(200), unique=True) 
    repo_path = Column(Unicode(200), unique=True)
    description = Column(UnicodeText)
 
 
    '''
    def __init__(self, repo_name='', repo_path='', description=''):
      
      self.repo_name = repo_name
      self.repo_path = repo_path
      self.description = description
      
   ''' 
 
      