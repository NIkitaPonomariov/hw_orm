from sqlalchemy import func, desc
from models import Student, Grade, Subject, Teacher
from sqlalchemy.orm import sessionmaker

def select_1(session):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

# Інші запити аналогічно, можна адаптувати під інші вимоги.
