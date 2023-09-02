#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (
    create_engine, Column, DateTime, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())  # Add the 'email' column
    grade = Column(Integer())  # Add the 'grade' column
    birthday = Column(DateTime)  # Add the 'birthday' column

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    albert_einstein = Student(
        name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )

    alan_turing = Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )

    session.bulk_save_objects([albert_einstein, alan_turing])
    session.commit()

    students_name=session.query(
        Student.name).order_by(Student.name).all()
    #print(students_name)

    query = session.query(Student).filter(Student.name.like('%Alan%'),
        Student.grade == 11).all()

    for record in query:
        #print(record.name)


        query = session.query(
        Student).filter(
            Student.name == "Albert Einstein")

    albert_einstein = query.first()
    session.delete(albert_einstein)
    session.commit()   
    print(albert_einstein) 