from rest_framework import serializers
from .models import CustomUser, OfficeStaffProfile, LibrarianProfile, Student, LibraryHistory, FeesHistory


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


class OfficeStaffProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = OfficeStaffProfile
        fields = '_all_'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        office_staff = OfficeStaffProfile.objects.create(user=user, **validated_data)
        return office_staff


class LibrarianProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = LibrarianProfile
        fields = ['id', 'user', 'phone_number', 'library_assigned', 'date_joined']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        librarian = LibrarianProfile.objects.create(user=user, **validated_data)
        return librarian
    

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '_all_'


class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = '_all_'

class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = '_all_'
