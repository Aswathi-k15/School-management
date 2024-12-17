# serializers.py
from rest_framework import serializers
from .models import LibraryHistory
from student.models import *

class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = '_all_'
        
class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'age', 'phone_number', 'class_name', 'address']
