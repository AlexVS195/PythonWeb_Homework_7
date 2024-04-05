from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Subject, Teacher, Group, engine

# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return result

# Знайти студента із найвищим середнім балом з певного предмета
def select_2(subject_name):
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Grade).join(Subject).filter(Subject.name == subject_name) \
        .group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
    return result

# Знайти середній бал у групах з певного предмета
def select_3(subject_name):
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name) \
        .group_by(Group.id).order_by(Group.name).all()
    return result

# Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()
    return result

# Знайти які курси читає певний викладач
def select_5(teacher_name):
    result = session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all()
    return result

# Знайти список студентів у певній групі
def select_6(group_name):
    result = session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()
    return result

# Знайти оцінки студентів у окремій групі з певного предмета
def select_7(group_name, subject_name):
    result = session.query(Student.fullname, Grade.grade) \
        .join(Group).join(Grade).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()
    return result

# Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(teacher_name):
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Subject).join(Teacher).filter(Teacher.name == teacher_name).scalar()
    return result

# Знайти список курсів, які відвідує певний студент
def select_9(student_name):
    result = session.query(Subject.name).join(Student).filter(Student.fullname == student_name).all()
    return result

# Список курсів, які певному студенту читає певний викладач
def select_10(student_name, teacher_name):
    result = session.query(Subject.name).join(Teacher).join(Grade).join(Student) \
        .filter(Student.fullname == student_name, Teacher.name == teacher_name).all()
    return result