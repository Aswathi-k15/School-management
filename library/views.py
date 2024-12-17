from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LibraryHistory
from .serializers import LibraryHistorySerializer
from django.shortcuts import get_object_or_404

class LibraryHistoryListCreateAPIView(APIView):
    """
    Handles GET (list all) and POST (create) requests.
    """
    def get(self, request):
        library_history = LibraryHistory.objects.all()
        serializer = LibraryHistorySerializer(library_history, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LibraryHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibraryHistoryDetailAPIView(APIView):
    """
    Handles GET (retrieve), PUT (update), and DELETE requests for individual items.
    """
    def get_object(self, pk):
        return get_object_or_404(LibraryHistory, pk=pk)

    def get(self, request, pk):
        library_history = self.get_object(pk)
        serializer = LibraryHistorySerializer(library_history)
        return Response(serializer.data)

    def put(self, request, pk):
        library_history = self.get_object(pk)
        serializer = LibraryHistorySerializer(library_history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        library_history = self.get_object(pk)
        library_history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)