from django.db import models
from django.contrib.auth.models import User
import datetime

class courtBooking(models.Model):

'''
Sport - Choices
Date - Datetime
Time - Time...Choices based off open court times per sport
Location - ?
Court - Based off Sport-specific court numbers
Singles/Doubles - Opens 2 Players or 4 Players
Player1 - OneToOne relationship?
Player2 - OneToOne relationship?
Player3 - OneToOne relationship?
Player4 - OneToOne relationship?
Comments - Text Field
Admin Notes - Text Field
Notification Emails - Y/N that automates sending emails based off any changes
'''