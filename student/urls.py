from django.urls import path
from .views import StudentEditView, StudentListView, StudentRegistrationView, StudentLoginView

urlpatterns = [
    path('register/', StudentRegistrationView.as_view(), name='student-register'),
    path('edit/<int:student_id>/', StudentEditView.as_view(), name='student-edit'),
    path('login/', StudentLoginView.as_view(), name='student-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),  # type: ignore
    path('students/', StudentListView.as_view(), name='student-list'),
]

