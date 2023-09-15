#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usatou"""

from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    connection_string = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(connection_string)

    Session = sessionmaker(bind=engine)
    session = Session()

    st_cty = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in st_cty:
        print(f"{state.name}: ({city.id}) {city.name}")
