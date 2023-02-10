from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MALE = "m"
    FEMALE = "f"
    SEX = [("MALE", "Male"), ("FEMALE", "F email")]

    HR = "hr"
    EMPLOYEE = "employee"
    UNKNOWN = "unknown"
    ROLE = [(HR, HR), (EMPLOYEE, EMPLOYEE), (UNKNOWN, UNKNOWN)]

    sex = models.CharField(max_length=6, choices=SEX, default=MALE)
    role = models.CharField(max_length=8, choices=ROLE, default=UNKNOWN)
