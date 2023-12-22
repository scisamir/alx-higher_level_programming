#!/usr/bin/python3
"""
City States relationship SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'
                .format(argv[1], argv[2], argv[3]),
                pool_pre_ping=True
            )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_sc = State(name='California', cities=[City(name='San Francisco')])

    session.add(new_sc)
    session.commit()
    session.close()
