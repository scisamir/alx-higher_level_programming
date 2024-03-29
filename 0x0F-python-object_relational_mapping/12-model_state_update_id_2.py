#!/usr/bin/python3
"""
Update a state via SQLAlchemy
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

    ud_state = session.query(State).filter_by(id=2).first()
    ud_state.name = 'New Mexico'
    session.commit()
