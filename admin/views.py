from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import OfficeStaffProfile, LibrarianProfile, Student
from .serializers import (
    OfficeStaffProfileSerializer,
    LibrarianProfileSerializer,
    StudentDetailSerializer,
)


# ViewSet for OfficeStaffProfile
class OfficeStaffProfileViewSet(viewsets.ModelViewSet):
    queryset = OfficeStaffProfile.objects.all()
    serializer_class = OfficeStaffProfileSerializer


# ViewSet for LibrarianProfile
class LibrarianProfileViewSet(viewsets.ModelViewSet):
    queryset = LibrarianProfile.objects.all()
    serializer_class = LibrarianProfileSerializer


# APIView for listing students
class StudentListView(APIView):
    permission_classes = [IsAuthenticated]  # Correct indentation

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentDetailSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import LibraryHistory
from .serializers import LibraryHistorySerializer

class LibraryHistoryViewSet(ReadOnlyModelViewSet):
    """
    ViewSet for read-only access to LibraryHistory records.
    """
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import FeesHistory
from .serializers import FeesHistorySerializer

class FeesHistoryViewSet(viewsets.ViewSet):
    def list(self, request):
        fees_history = FeesHistory.objects.all()
        serializer = FeesHistorySerializer(fees_history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser

def user_login(request):
    if request.method == 'POST':
        # Get username and password from POST request
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            
            # Redirect user based on role
            if user.role == 'LIBRARIAN':
                return redirect('librarian_dashboard')  # Redirect to librarian's dashboard
            elif user.role == 'OFFICE_STAFF':
                return redirect('office_staff_dashboard')  # Redirect to office staff's dashboard
            else:
                return redirect('admin_dashboard')  # Redirect to admin's dashboard
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'accounts/login.html')
    
    return render(request, 'accounts/login.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout