from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="person")
    person_firstname = models.CharField(max_length=100, blank=True, null=True)
    person_middlename = models.CharField(max_length=100, blank=True, null=True)
    person_lastname = models.CharField(max_length=100, blank=True, null=True)
    person_age = models.IntegerField(default=0)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    person_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    person_contact = models.CharField(max_length=11, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.person_firstname} {self.person_lastname}".strip() or self.user.username
