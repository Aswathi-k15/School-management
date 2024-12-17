from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from school.student.models import Student, StudentEditSerializer
from .serializers import StudentRegistrationSerializer, StudentLoginSerializer

class StudentRegistrationView(APIView):
    def post(self, request):
        serializer = StudentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import Student
from .serializers import StudentLoginSerializer

class StudentLoginView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            student = Student.objects.get(name=name)

            # Generate JWT Token
            refresh = RefreshToken.for_user(student)

            return Response({
                "message": "Login successful.",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "student_id": student.student_id,
                "name": student.name
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentEditView(APIView):
    def get_object(self, student_id):
        try:
            return Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            return None

    def put(self, request, student_id):
        student = self.get_object(student_id)
        if not student:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentEditSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Details updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentDetailSerializer

class StudentListView(APIView):
permission_classes = [IsAuthenticated] # type: ignore
def get(self, request):
        students = Student.objects.all()
        serializer = StudentDetailSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)