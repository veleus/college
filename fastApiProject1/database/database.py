from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fio = Column(String, nullable=False)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    academic_name = Column(String)

class Academic(Base):
    __tablename__ = 'academics'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    mark = Column(String, nullable=False)
    semester = Column(String, nullable=False)
    academic_name= Column(String,  nullable=False)
    teacher_name = Column(String, nullable=False)
    student_name = Column(String,  nullable=False)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fio = Column(String, nullable=False)
    group_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    snils = Column(String, nullable=False)
    god_postupleniya = Column(String, nullable=False)
    passport = Column(String, nullable=False)



class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    short_name = Column(String, nullable=False, unique=True)
    full_name = Column(String, nullable=False, unique=True)

