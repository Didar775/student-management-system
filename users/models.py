from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin',
    TEACHER = 'teacher',
    STUDENT = 'student',

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    ]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default=STUDENT)

