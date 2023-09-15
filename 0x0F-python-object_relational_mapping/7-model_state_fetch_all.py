#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State)

for state in states:
    print(f"{state.id}: {state.name}")
