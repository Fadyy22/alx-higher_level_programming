#!/usr/bin/python3
"""script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, or_
from sys import argv

if __name__ == "__main__":
    connection_string = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(connection_string)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == f"{argv[4]}").first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
