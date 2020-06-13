from django.urls import path
from .views import tennisListView
from . import views

urlpatterns = [
    path('tennis/', tennisListView.as_view(), name='booking-tennis'),
]