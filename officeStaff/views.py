from django.shortcuts import render
from fastapi import Response
from streamlit import status

from school.officeStaff.serializers import StudentDetailSerializer
from school.student.models import Student

# Create your views here.
class StudentListView(APIView): # type: ignore
permission_classes = [IsAuthenticated] # type: ignore
def get(self, request):
        students = Student.objects.all()
        serializer = StudentDetailSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



from rest_framework.viewsets import ModelViewSet
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated

class ReviewViewSet(ModelViewSet):
    """
    Viewset for handling CRUD operations on reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically associate the logged-in user with the review.
        """
        serializer.save(user=self.request.user)