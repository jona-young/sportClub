from django.shortcuts import render
from .models import

def tennisBooking(request):
    context = {
        #TODO: Filter so that only court bookings with 'Tennis' sport specification are selected
        #'tennis': courtBooking.objects.all()
    }

    #Set the template that redirects to the tennis booking page
    #return render(request, 'bookings/', context)



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

