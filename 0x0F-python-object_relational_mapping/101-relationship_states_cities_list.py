#!/usr/bin/python3
"""
List relationship SQLAlchemy
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

    my_state = session.query(State).order_by(State.id).all()

    for st in my_state:
        print(f"{st.id}: {st.name}")
        for ct in st.cities:
            print(f"\t {ct.id}: {ct.name}")
