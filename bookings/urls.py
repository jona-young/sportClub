from django.urls import path
from .views import TennisDetailView, TennisCreateView, TennisUpdateView, TennisDeleteView
from . import views

urlpatterns = [
    path('tennis/<int:pk>/', TennisDetailView.as_view(), name='detail-tennis'),
    path('tennis/<int:pk>/update', TennisUpdateView.as_view(), name='update-tennis'),
    path('tennis/<int:pk>/delete', TennisDeleteView.as_view(), name='delete-tennis'),
    path('tennis/new/', TennisCreateView.as_view(), name='create-tennis'),
    path('tennis/', views.tennisScheduleView, name='schedule-tennis'),
]