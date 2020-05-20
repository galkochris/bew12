from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from datetime import datetime

class Pet(models.Model):
    pet_name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    weight_in_pounds = models.IntegerField(max_length=5)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pet_name

class Appointment(models.Model):
    date_of_appointment = models.DateField()
    duration_minutes = models.IntegerField(default=0, max_length=3)
    special_instructions = models.CharField(null=True, max_length=200)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False)

