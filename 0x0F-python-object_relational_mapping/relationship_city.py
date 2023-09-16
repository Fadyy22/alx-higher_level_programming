#!/usr/bin/python3
"""class definition of a City"""

from relationship_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """class City that defines a cities table in db"""

    __tablename__ = "cities"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
