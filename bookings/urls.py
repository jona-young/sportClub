from django.urls import path
from . import views

urlpatterns = [
    path('tennis/', views.tennisBooking, name='booking-tennis'),
]