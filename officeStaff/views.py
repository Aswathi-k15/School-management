from django.shortcuts import render
from fastapi import Response
from streamlit import status
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.permissions import IsAuthenticated
from school.officeStaff.serializers import *
from school.student.models import Student

# Create your views here.
class StudentListView(APIView): # type: ignore
permission_classes = [IsAuthenticated] # type: ignore
def get(self, request):
        students = Student.objects.all()
        serializer = StudentDetailSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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

class FeesHistoryListCreateAPIView(APIView):
    def get(self, request):
        fees_history = FeesHistory.objects.all()
        serializer = FeesHistorySerializer(fees_history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FeesHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeesHistoryDetailAPIView(APIView):
    def get(self, request, pk):
        fees_history = get_object_or_404(FeesHistory, pk=pk)
        serializer = FeesHistorySerializer(fees_history)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        fees_history = get_object_or_404(FeesHistory, pk=pk)
        serializer = FeesHistorySerializer(fees_history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        fees_history = get_object_or_404(FeesHistory, pk=pk)
        fees_history.delete()
        return Response({"message": "Fee record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
