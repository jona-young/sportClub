from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
import datetime

class Members(models.Model):
    memberNum = models.OneToOneField(User, on_delete=models.CASCADE)
    memberLink = models.CharField(max_length=20)
    memberLevel = models.CharField(max_length=20)
    memberBegins = models.DateTimeField(default=datetime.datetime.now())
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    gender = models.CharField(max_length=2, choices=[('ML', 'Male'), ('FL', 'Female'), ('OT', 'Other')])
    birthDate = models.DateField(default=datetime.datetime.now())
    emailAddress = models.CharField(max_length=40)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    province = models.CharField(max_length=40)
    postalCode = models.CharField(max_length=7)
    country = CountryField()
    homePhone = PhoneNumberField()
    cellPhone = PhoneNumberField()
    workPhone = PhoneNumberField()
    tennisRank = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    squashRank = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    badmintonRank = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    platformRank = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)


    def __str__(self):
        return '{} {} - {}'.format(self.firstName, self.lastName, self.memberNum)

#TODO
'''
Python Django Tutorial Part 10 - Create, Update, and Delete Posts

Is this applicable for me?  Court Bookings maybe?
'''
'''
You have to link the User model user to each Members model per person in order to display that information
'''

'''
How will Create, Update, Delete module affect a sport booking website?

How can you create a booking database that is used both for events and normal court bookings?  Could use a
form field that identifies if it is an event entry or a court booking entry.  A current issue is booking
events on the Program Registration Calendar is separate from booking website.  If you register an event
that requires sport courts, you have to manually block off courts in the court booking side.  Shared 
names for title on Program Reg Calendar could be called 'Event Title' but Court Booking would default to
'Court Booking for X Sport'...or what other situations?

How can a court booking form adjust based off which sport you are booking for?  Two form fields one that
designates a sport..if that sport is chosen, the second form field adjusts to specifically courts that
are designated for that sport.  One to Many Field? ForeignKey? How do I link that relationship?

First thing is create a basic court booking database and then if needed you can adjust the court booking
database to include events in a separate git branch.
'''