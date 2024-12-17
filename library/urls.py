# urls.py
from django.urls import path
from .views import LibraryHistoryListCreateAPIView, LibraryHistoryDetailAPIView

urlpatterns = [
    path('library-history/', LibraryHistoryListCreateAPIView.as_view(), name='library-history-list-create'),
    path('library-history/<int:pk>/', LibraryHistoryDetailAPIView.as_view(), name='library-history-detail'),
]