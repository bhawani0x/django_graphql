import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_graphql.settings")
django.setup()

import random
from faker import Faker
from django.utils import timezone
from models import Class, Student

fake = Faker()


# Generate fake Class data
def create_fake_class():
    class_name = fake.word()
    teacher_name = fake.name()
    teacher_number = fake.random_number(digits=10)
    new_class = Class.objects.create(
        name=class_name,
        Class_teacher_name=teacher_name,
        class_teacher_number=teacher_number
    )
    return new_class


# Generate fake Student data
def create_fake_student(class_instance):
    first_name = fake.first_name()
    last_name = fake.last_name()
    dob = fake.date_of_birth(minimum_age=17, maximum_age=45)
    father_name = fake.name()
    address = fake.address()
    new_student = Student.objects.create(
        Class=class_instance,
        first_name=first_name,
        last_name=last_name,
        dob=dob,
        Father_name=father_name,
        address=address
    )
    return new_student


if __name__ == '__main__':
    # Generate fake data for 10 classes and 50 students in each class
    for _ in range(10):
        new_class = create_fake_class()
        for _ in range(50):
            create_fake_student(new_class)
