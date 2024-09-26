from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade
import random
from datetime import datetime

fake = Faker()

engine = create_engine('postgresql://username:password@localhost/mydatabase')
Session = sessionmaker(bind=engine)
session = Session()

# Створюємо групи
groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

# Створюємо викладачів
teachers = [Teacher(fullname=fake.name()) for _ in range(4)]
session.add_all(teachers)
session.commit()

# Створюємо предмети
subjects = [Subject(name=fake.job(), teacher=random.choice(teachers)) for _ in range(6)]
session.add_all(subjects)
session.commit()

# Створюємо студентів
students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

# Створюємо оцінки
for student in students:
    for subject in subjects:
        for _ in range(random.randint(10, 20)):
            grade = Grade(student=student, subject=subject, grade=random.uniform(60, 100), date_received=datetime.now())
            session.add(grade)

session.commit()
