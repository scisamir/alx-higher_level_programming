#!/usr/bin/python3
"""
Get a state by name via SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'
                .format(argv[1], argv[2], argv[3]),
                pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    the_state = session.query(State).filter(State.name == argv[4]).first()
    if the_state:
        print(the_state.id)
    else:
        print('Not found')
