#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usatou"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    connection_string = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(connection_string)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).all()
    for state in st:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
