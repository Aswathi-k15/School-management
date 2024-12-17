from django.urls import path, include
from rest_framework.routers import DefaultRouter

from school.student import views
from .views import OfficeStaffProfileViewSet, LibrarianProfileViewSet, StudentListView

router = DefaultRouter()
router.register(r'office-staff', OfficeStaffProfileViewSet)
router.register(r'librarian', LibrarianProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('logout/', views.user_logout, name='logout'),

]