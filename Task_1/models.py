from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from faker import Faker
import random
from datetime import datetime

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", back_populates="group")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship("Subject", back_populates="teacher")

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship("Teacher", back_populates="subjects")

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    grade = Column(Integer, nullable=False)
    grade_date = Column(Date, nullable=False)

    student = relationship("Student", back_populates="grades")

# З'єднання з базою даних PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:GoITHomework7@localhost:5432/Homework7')

# Створення таблиць у базі даних
Base.metadata.create_all(engine)

# Створення фабрики сесій
Session = sessionmaker(bind=engine)

# Створення випадкових даних за допомогою Faker
fake = Faker()

# Заповнення бази даних випадковими даними
session = Session()

# Створення груп
groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

# Створення викладачів
teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

# Створення предметів
subjects = [Subject(name=f"Subject {i}", teacher=random.choice(teachers)) for i in range(1, 9)]
session.add_all(subjects)
session.commit()

# Створення студентів та їх оцінок
for _ in range(30):
    student = Student(name=fake.name(), group=random.choice(groups))
    session.add(student)
    session.commit()  

    for subject in subjects:
        grade = random.randint(1, 100)
        grade_date = fake.date_between(start_date='-1y', end_date='today')
        grade_entry = Grade(student_id=student.id, subject_id=subject.id, grade=grade, grade_date=grade_date)
        session.add(grade_entry)

session.commit()

session.close()