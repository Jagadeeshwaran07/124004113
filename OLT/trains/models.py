
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10, unique=True)
    owner_email = models.EmailField(unique=True)
    access_code = models.CharField(max_length=20)
    client_id = models.UUIDField(unique=True)
    client_secret = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Train(models.Model):
    name = models.CharField(max_length=100)
    train_number = models.CharField(max_length=10)
    departure_time = models.DateTimeField()
    seats_available_sleeper = models.PositiveIntegerField()
    seats_available_ac = models.PositiveIntegerField()
    price_sleeper = models.DecimalField(max_digits=10, decimal_places=2)
    price_ac = models.DecimalField(max_digits=10, decimal_places=2)
    delayed_by = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
