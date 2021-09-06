import calendar
from django.db import models


class Questionnare(models.Model):
    DAY_CHOICES = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday")
    ]

    MONTH_CHOICES = [(value, calendar.month_name[value]) for value in range(1, 13)]

    month = models.IntegerField(choices=MONTH_CHOICES)
    day = models.IntegerField(choices=DAY_CHOICES)
