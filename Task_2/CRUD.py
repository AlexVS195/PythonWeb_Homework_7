import argparse
from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
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

# Створення фабрики сесій
Session = sessionmaker(bind=engine)

def create_teacher(args):
    session = Session()
    new_teacher = Teacher(name=args.name)
    session.add(new_teacher)
    session.commit()
    session.close()
    print(f"Teacher '{args.name}' created successfully.")

def list_teachers(args):
    session = Session()
    teachers = session.query(Teacher).all()
    session.close()
    if teachers:
        print("List of teachers:")
        for teacher in teachers:
            print(f"ID: {teacher.id}, Name: {teacher.name}")
    else:
        print("No teachers found.")

def update_teacher(args):
    session = Session()
    teacher = session.query(Teacher).filter_by(id=args.id).first()
    if teacher:
        teacher.name = args.name
        session.commit()
        print(f"Teacher {args.id} updated successfully.")
    else:
        print(f"Teacher with ID {args.id} not found.")
    session.close()

def remove_teacher(args):
    session = Session()
    teacher = session.query(Teacher).filter_by(id=args.id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher {args.id} removed successfully.")
    else:
        print(f"Teacher with ID {args.id} not found.")
    session.close()

def create_group(args):
    session = Session()
    new_group = Group(name=args.name)
    session.add(new_group)
    session.commit()
    session.close()
    print(f"Group '{args.name}' created successfully.")

def list_groups(args):
    session = Session()
    groups = session.query(Group).all()
    session.close()
    if groups:
        print("List of groups:")
        for group in groups:
            print(f"ID: {group.id}, Name: {group.name}")
    else:
        print("No groups found.")

def update_group(args):
    session = Session()
    group = session.query(Group).filter_by(id=args.id).first()
    if group:
        group.name = args.name
        session.commit()
        print(f"Group {args.id} updated successfully.")
    else:
        print(f"Group with ID {args.id} not found.")
    session.close()

def remove_group(args):
    session = Session()
    group = session.query(Group).filter_by(id=args.id).first()
    if group:
        session.delete(group)
        session.commit()
        print(f"Group {args.id} removed successfully.")
    else:
        print(f"Group with ID {args.id} not found.")
    session.close()

def create_subject(args):
    session = Session()
    teacher = session.query(Teacher).filter_by(id=args.teacher_id).first()
    if not teacher:
        print(f"Teacher with ID {args.teacher_id} not found.")
        return

    new_subject = Subject(name=args.name, teacher_id=args.teacher_id)
    session.add(new_subject)
    session.commit()
    session.close()
    print(f"Subject '{args.name}' created successfully.")

def list_subjects(args):
    session = Session()
    subjects = session.query(Subject).all()
    session.close()
    if subjects:
        print("List of subjects:")
        for subject in subjects:
            print(f"ID: {subject.id}, Name: {subject.name}, Teacher ID: {subject.teacher_id}")
    else:
        print("No subjects found.")

def update_subject(args):
    session = Session()
    subject = session.query(Subject).filter_by(id=args.id).first()
    if subject:
        subject.name = args.name
        subject.teacher_id = args.teacher_id
        session.commit()
        print(f"Subject {args.id} updated successfully.")
    else:
        print(f"Subject with ID {args.id} not found.")
    session.close()

def remove_subject(args):
    session = Session()
    subject = session.query(Subject).filter_by(id=args.id).first()
    if subject:
        session.delete(subject)
        session.commit()
        print(f"Subject {args.id} removed successfully.")
    else:
        print(f"Subject with ID {args.id} not found.")
    session.close()

def create_student(args):
    session = Session()
    group = session.query(Group).filter_by(id=args.group_id).first()
    if not group:
        print(f"Group with ID {args.group_id} not found.")
        return

    new_student = Student(name=args.name, group_id=args.group_id)
    session.add(new_student)
    session.commit()
    session.close()
    print(f"Student '{args.name}' created successfully.")

def list_students(args):
    session = Session()
    students = session.query(Student).all()
    session.close()
    if students:
        print("List of students:")
        for student in students:
            print(f"ID: {student.id}, Name: {student.name}, Group ID: {student.group_id}")
    else:
        print("No students found.")

def update_student(args):
    session = Session()
    student = session.query(Student).filter_by(id=args.id).first()
    if student:
        student.name = args.name
        student.group_id = args.group_id
        session.commit()
        print(f"Student {args.id} updated successfully.")
    else:
        print(f"Student with ID {args.id} not found.")
    session.close()

def remove_student(args):
    session = Session()
    student = session.query(Student).filter_by(id=args.id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student {args.id} removed successfully.")
    else:
        print(f"Student with ID {args.id} not found.")
    session.close()

def create_grade(args):
    session = Session()
    student = session.query(Student).filter_by(id=args.student_id).first()
    if not student:
        print(f"Student with ID {args.student_id} not found.")
        return

    subject = session.query(Subject).filter_by(id=args.subject_id).first()
    if not subject:
        print(f"Subject with ID {args.subject_id} not found.")
        return

    new_grade = Grade(student_id=args.student_id, subject_id=args.subject_id, grade=args.grade, grade_date=args.grade_date)
    session.add(new_grade)
    session.commit()
    session.close()
    print(f"Grade for Student ID {args.student_id} and Subject ID {args.subject_id} created successfully.")

def list_grades(args):
    session = Session()
    grades = session.query(Grade).all()
    session.close()
    if grades:
        print("List of grades:")
        for grade in grades:
            print(f"ID: {grade.id}, Student ID: {grade.student_id}, Subject ID: {grade.subject_id}, Grade: {grade.grade}, Date: {grade.grade_date}")
    else:
        print("No grades found.")

def update_grade(args):
    session = Session()
    grade = session.query(Grade).filter_by(id=args.id).first()
    if grade:
        grade.student_id = args.student_id
        grade.subject_id = args.subject_id
        grade.grade = args.grade
        grade.grade_date = args.grade_date
        session.commit()
        print(f"Grade {args.id} updated successfully.")
    else:
        print(f"Grade with ID {args.id} not found.")
    session.close()

def remove_grade(args):
    session = Session()
    grade = session.query(Grade).filter_by(id=args.id).first()
    if grade:
        session.delete(grade)
        session.commit()
        print(f"Grade {args.id} removed successfully.")
    else:
        print(f"Grade with ID {args.id} not found.")
    session.close()

def main():
    parser = argparse.ArgumentParser(description='CRUD operations with database')
    parser.add_argument('--action', '-a', choices=['create', 'list', 'update', 'remove'], required=True, help='Action to perform (create, list, update, remove)')
    parser.add_argument('--model', '-m', choices=['Teacher', 'Group', 'Subject', 'Student', 'Grade'], required=True, help='Model to perform action on (Teacher, Group, Subject, Student, Grade)')
    parser.add_argument('--id', type=int, help='ID of the entity')
    parser.add_argument('--name', type=str, help='Name of the entity')
    parser.add_argument('--teacher_id', type=int, help='Teacher ID for Subject model')
    parser.add_argument('--group_id', type=int, help='Group ID for Student model')
    parser.add_argument('--subject_id', type=int, help='Subject ID for Grade model')
    parser.add_argument('--grade', type=int, help='Grade for Grade model')
    parser.add_argument('--grade_date', type=str, help='Grade date for Grade model')

    args = parser.parse_args()

    if args.model == 'Teacher':
        if args.action == 'create':
            create_teacher(args)
        elif args.action == 'list':
            list_teachers(args)
        elif args.action == 'update':
            update_teacher(args)
        elif args.action == 'remove':
            remove_teacher(args)
    elif args.model == 'Group':
        if args.action == 'create':
            create_group(args)
        elif args.action == 'list':
            list_groups(args)
        elif args.action == 'update':
            update_group(args)
        elif args.action == 'remove':
            remove_group(args)
    elif args.model == 'Subject':
        if args.action == 'create':
            create_subject(args)
        elif args.action == 'list':
            list_subjects(args)
        elif args.action == 'update':
            update_subject(args)
        elif args.action == 'remove':
            remove_subject(args)
    elif args.model == 'Student':
        if args.action == 'create':
            create_student(args)
        elif args.action == 'list':
            list_students(args)
        elif args.action == 'update':
            update_student(args)
        elif args.action == 'remove':
            remove_student(args)
    elif args.model == 'Grade':
        if args.action == 'create':
            create_grade(args)
        elif args.action == 'list':
            list_grades(args)
        elif args.action == 'update':
            update_grade(args)
        elif args.action == 'remove':
            remove_grade(args)

if __name__ == '__main__':
    main()