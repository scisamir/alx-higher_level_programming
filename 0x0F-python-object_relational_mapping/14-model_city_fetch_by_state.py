#!/usr/bin/python3
"""
Cities in  states via SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'
                .format(argv[1], argv[2], argv[3]),
                pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    state_cities = session.query(State.name, City.id, City.name)\
        .join(City, State.id == City.state_id).order_by(City.id).all()

    for sc in state_cities:
        print(f"{sc[0]}: ({sc[1]}) {sc[2]}")
