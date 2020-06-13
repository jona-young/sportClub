from django.shortcuts import render
from .models import courtBooking
from django.views.generic import ListView


class tennisListView(ListView):
    model = courtBooking
    template_name = 'bookings/tennis.html'
    context_object_name = 'bookings'

#TODO:
'''

For each sport booking page, the 'context' passed to the views template will have to pull from the court
booking database through filter of a form field for the specific sport

Tennis
Squash
Badminton & Pickleball
Platform Tennis
Table Tennis
Golf Simulator

'''

