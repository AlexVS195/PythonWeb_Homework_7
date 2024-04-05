from sqlalchemy import func

# Середній бал, який певний викладач ставить певному студентові.
def average_grade_for_student_by_teacher(student_id, teacher_id, session):
    query = session.query(func.avg(Grade.grade)). \
        filter(Grade.student_id == student_id). \
        filter(Subject.teacher_id == teacher_id). \
        join(Subject, Grade.subject_id == Subject.id). \
        join(Teacher, Subject.teacher_id == Teacher.id)

    average_grade = query.scalar()
    return average_grade

# Оцінки студентів у певній групі з певного предмета на останньому занятті.
def grades_for_students_in_group_on_last_lesson(group_id, subject_id, session):
    query = session.query(Grade). \
        filter(Student.group_id == group_id). \
        filter(Grade.subject_id == subject_id). \
        order_by(Grade.grade_date.desc()). \
        limit(1)

    last_lesson_grades = query.all()
    return last_lesson_grades
