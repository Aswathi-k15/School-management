from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from .models import FeesHistory, Student

class StudentRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Student
        fields = ['name', 'age', 'phone_number', 'password', 'confirm_password', 'class_name', 'address']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password
        return Student.objects.create(**validated_data)

class StudentEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['age', 'phone_number', 'class_name', 'address']



class StudentLoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            student = Student.objects.get(name=data['name'])
        except Student.DoesNotExist:
            raise serializers.ValidationError({"name": "User does not exist."})

        if not check_password(data['password'], student.password):
            raise serializers.ValidationError({"password": "Invalid password."})

        return {"name": student.name, "student_id": student.student_id}
    




