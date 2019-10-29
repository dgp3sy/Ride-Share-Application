from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Ride(models.Model):
    origin = models.CharField(max_length=50)
    origin_state = models.CharField(max_length=50, default="N/A")
    destination = models.CharField(max_length=50)
    destination_state = models.CharField(max_length=50, default="N/A")
    departure_date = models.DateField()
    seats_available = models.IntegerField(choices = [(i,i) for i in range(1,6)])
    def __str__(self):
        return '%s %s %s' % (self.origin, self.destination, self.departure_date)

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created: #interpret as "new user" 
        Profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

