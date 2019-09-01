from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)


class Reservation(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.PROTECT, related_name="reservations"
    )
    date = models.DateField()
    is_valid = models.BooleanField(default=True)
