#!usr/bin/python3
"""A script that lists only the first State object from the database hbtn_0e_6_usa """

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

first_state = session.query(State).order_by(State.id).first()
if first_state is not None:
    print("{}: {}".format(first_state.id, first_state.name))
else:
    print('Nothing')
session.close()
