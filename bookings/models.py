from django.db import models
from django.contrib.auth.models import User
import datetime

class courtBooking(models.Model):
    sportChoice = [
        ('TN', 'Tennis'),
        ('SQ', 'Squash'),
        ('BP', 'Badminton / Pickleball'),
        ('PT', 'Platform Tennis'),
    ]

    courtTime = [
        ('5:40 AM', '5:40 AM'),
        ('6:00 AM', '6:00 AM'),
        ('6:20 AM', '6:20 AM'),
        ('7:00 AM', '7:00 AM'),
        ('7:40 AM', '7:40 AM'),
        ('8:00 AM', '8:00 AM'),
        ('8:20 AM', '8:20 AM'),
        ('9:00 AM', '9:00 AM'),
        ('9:40 AM', '9:40 AM'),
        ('10:00 AM', '10:00 AM'),
        ('10:20 AM', '10:20 AM'),
        ('11:00 AM', '11:00 AM'),
        ('11:40 AM', '11:40 AM'),
        ('12:00 PM', '12:00 PM'),
        ('12:15 PM', '12:15 PM'),
        ('12:20 PM', '12:20 PM'),
        ('1:00 PM', '1:00 PM'),
        ('1:15 PM', '1:15 PM'),
        ('1:40 PM', '1:40 PM'),
        ('2:00 PM', '2:00 PM'),
        ('2:15 PM', '2:15 PM'),
        ('2:20 PM', '2:20 PM'),
        ('3:00 PM', '3:00 PM'),
        ('3:30 PM', '3:30 PM'),
        ('3:40 PM', '3:40 PM'),
        ('4:00 PM', '4:00 PM'),
        ('4:20 PM', '4:20 PM'),
        ('4:30 PM', '4:30 PM'),
        ('5:00 PM', '5:00 PM'),
        ('5:30 PM', '5:30 PM'),
        ('5:40 PM', '5:40 PM'),
        ('6:00 PM', '6:00 PM'),
        ('6:20 PM', '6:20 PM'),
        ('6:30 PM', '6:30 PM'),
        ('7:00 PM', '7:00 PM'),
        ('7:30 PM', '7:30 PM'),
        ('7:40 PM', '7:40 PM'),
        ('8:00 PM', '8:00 PM'),
        ('8:20 PM', '8:20 PM'),
        ('8:30 PM', '8:30 PM'),
        ('9:00 PM', '9:00 PM'),
        ('9:30 PM', '9:30 PM'),
        ('9:40 PM', '9:40 PM'),
    ]

    sport = models.CharField(max_length=2, choices=sportChoice)
    courtDate = models.DateField(default=datetime.datetime.now())
    courtTime = models.CharField(max_length=8, choices=courtTime)
    courtLocation = models.CharField(max_length=3, choices=[('B&R', 'B&R'), ('UCC', 'UCC')])
    courtNumber = models.CharField(max_length=1, choices=[
        ('1', 'Court 1'),
        ('2', 'Court 2'),
        ('3', 'Court 3'),
        ('4', 'Court 4')
    ])
    courtPlay = models.CharField(max_length=2, choices=[('SN', 'Singles'), ('DB', 'Doubles')])
    player1 = models.ManyToManyField(User, related_name='player1')
    player2 = models.ManyToManyField(User, related_name='player2')
    player3 = models.ManyToManyField(User, related_name='player3', blank=True, null=True)
    player4 = models.ManyToManyField(User, related_name='player4', blank=True, null=True)
    comments = models.TextField(max_length=200)



    '''
    Sport - Choices
    Date - Datetime
    Time - Time...Choices based off open court times per sport
    Location - (?) B&R or UCC
    Court - Based off Sport-specific court numbers
    Singles/Doubles - Opens 2 Players or 4 Players
    Player1 - OneToOne relationship?
    Player2 - OneToOne relationship?
    Player3 - OneToOne relationship?
    Player4 - OneToOne relationship?
    Comments - Text Field
    Admin Notes - Text Field
    Notification Emails - Y/N that automates sending emails based off any changes

    Ideally would like to change court numbers based off sport and location...may be a front-end script
    where if 'value' from element is selected, adjust options for certain other form field.
    '''