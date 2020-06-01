from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Members(models.Model):
    memberNum = models.ForeignKey(User, on_delete=models.CASCADE)
    memberLink = models.CharField(max_length=20)
    memberLevel = models.CharField(max_length=20)
    memberBegins = models.DateTimeField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    gender = models.CharField(max_length=2, choices=[('ML', 'Male'), ('FL', 'Female'), ('OT', 'Other')])
    birthDate = models.DateField()
    emailAddress = models.CharField(max_length=40)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    province = models.CharField(max_length=40)
    postalCode = models.CharField(max_length=7)
    country = CountryField()
    homePhone = models.CharField(max_length=14)
    cellPhone = models.CharField(max_length=14)
    workPhone = models.CharField(max_length=14)
    tennisRank = models.DecimalField(max_digits=3, decimal_places=2)
    squashRank = models.DecimalField(max_digits=3, decimal_places=2)
    badmintonRank = models.DecimalField(max_digits=3, decimal_places=2)
    platformRank = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return '{} {} - {}'.format(self.firstName, self.lastName, self.memberNum)

#TODO
'''
Python Django Tutorial Part 6 - User Registration...BEGINNING
Migrated models, added to admin panel, setup first template view.
'''