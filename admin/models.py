
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('OFFICE_STAFF', 'Office Staff'),
        ('LIBRARIAN', 'Librarian'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='OFFICE_STAFF')

class OfficeStaffProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='office_staff_profile')
    username=models.CharField(max_length=100) 
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=8)  # Added password field

    address = models.TextField()
    date_joined = models.DateField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} - Office Staff"
    
class LibrarianProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='librarian_profile')
    phone_number = models.CharField(max_length=15)
    username=models.CharField(max_length=100)
    password = models.CharField(max_length=8)  # Added password field
    library_assigned = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} - Librarian"
