from django.db import models


class Ride(models.Model):
    origin = models.CharField(max_length=50, blank=False)
    origin_state = models.CharField(max_length=50, default="N/A", blank=False)
    destination = models.CharField(max_length=50, blank=False)
    destination_state = models.CharField(max_length=50, default="N/A", blank=False)
    departure_date = models.DateField(blank=False)
    seats_available = models.IntegerField(choices = [(i,i) for i in range(1,6)])
    def __str__(self):
        return '%s %s %s' % (self.origin, self.destination, self.departure_date)
#
# class User(models.Model):
#     first_name = models.CharField(max_length=50, default="John")
#     last_name = models.CharField(max_length=50, default="Doe")
#     email = models.CharField(max_length=50)

# User-to-user messaging feature, url:https://stackoverflow.com/questions/32687461/how-to-create-a-user-to-user-message-system-using-django
# class Message(models.Model):
#     sender = models.ForeignKey(User, related_name="sender")
#     receiver = models.ForeignKey(User, related_name="receiver")
#     msg_content = models.CharField(max_length=640)
#     timestamp = models.DateTimeField(default=datetime.now)