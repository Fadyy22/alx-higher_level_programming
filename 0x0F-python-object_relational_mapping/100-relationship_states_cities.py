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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)

    session.add(state)
    session.add(city)
    session.commit()
