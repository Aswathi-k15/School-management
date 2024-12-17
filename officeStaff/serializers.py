from school.officeStaff.models import FeesHistory
from school.student import serializers
from school.student.models import Student
from .models import Review


class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = '_all_'

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'age', 'phone_number', 'class_name', 'address']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '_all_'
        read_only_fields = ['user', 'created_at', 'updated_at']  # Auto-set fields
