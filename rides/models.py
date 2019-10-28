from django.db import models


class Ride(models.Model):
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_date = models.CharField(max_length=50)
    seats_available = models.IntegerField()
    def __str__(self):
        return '%s %s %s' % (self.origin, self.destination, self.departure_date)

