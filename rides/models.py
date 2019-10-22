from django.db import models

class Ride(models.Model):
    origin = models.CharField(max_length=50)
    origin_state = models.CharField(max_length=50, default="N/A")
    destination = models.CharField(max_length=50)
    destination_state = models.CharField(max_length=50, default="N/A")
    departure_date = models.DateField()
    seats_available = models.IntegerField(choices = [(i,i) for i in range(1,6)])
    def __str__(self):
        return '%s %s %s' % (self.origin, self.destination, self.departure_date)
