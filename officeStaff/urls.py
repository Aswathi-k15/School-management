from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentEditView,
    StudentListView,
    StudentRegistrationView,
    StudentLoginView,
    ReviewViewSet
)

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')

# Define urlpatterns
urlpatterns = [
    # Class-based views for student-related endpoints
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/register/', StudentRegistrationView.as_view(), name='student-register'),
    path('students/login/', StudentLoginView.as_view(), name='student-login'),
    path('students/edit/<int:pk>/', StudentEditView.as_view(), name='student-edit'),

    # Include the router-generated URLs
    path('', include(router.urls)),
]
