#!usr/bin/python3
"""A script that lists all State objects from the database hbtn_0e_6_usa """

import sqlalchemy
from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],argv[2],argv[3]))

Base.metadata.create_all(eng)
Session = sessionmaker(bind=eng)
session = Session()

for state in session.query(State).order_by(State.id):
    print("{}: {}".format(state.id, state.name))
session.close()
