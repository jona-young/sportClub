# Generated by Django 3.0.2 on 2020-06-17 22:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20200617_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courtbooking',
            name='courtDate',
            field=models.DateField(default=datetime.datetime(2020, 6, 17, 22, 46, 52, 658575, tzinfo=utc)),
        ),
    ]
