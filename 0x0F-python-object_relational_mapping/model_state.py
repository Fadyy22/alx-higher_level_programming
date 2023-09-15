#!/usr/bin/python3
"""python file that contains the class definition of a State
and an instance Base = declarative_base()
using SQLAlchemy"""

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """class state that defines a state"""

    __tablename__ = "states"
    id = Column(autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
