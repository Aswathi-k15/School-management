from django.db import models
from django.contrib.auth.hashers import make_password

from school.student import serializers

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  # Store hashed passwords
    class_name = models.CharField(max_length=100)
    address = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk:  # Hash password only during creation
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def _str_(self):
        return self.name
    
