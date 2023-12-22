#!/usr/bin/python3
"""
From city relationship SQLAlchemy
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

    Session = sessionmaker(bind=engine)
    session = Session()

    my_city = session.query(City).order_by(City.id).all()

    for ct in my_city:
        print(f"{ct.id}: {ct.name} -> {ct.state.name}")
