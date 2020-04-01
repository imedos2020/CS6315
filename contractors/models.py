from django.db import models

# Create your models here.


class Contractor(models.Model):
    firstName = models.CharField(default='Joe', max_length=100)
    lastName = models.CharField(default='Average', max_length=100)
    skills = models.CharField(
        max_length=20, default='Housekeeper')
    availableNow = models.BooleanField(default=True)
