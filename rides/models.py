
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from datetime import date
from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator


class Ride(models.Model):
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.SET_NULL, null=True)
    id = models.AutoField(primary_key=True)
    origin = models.CharField(max_length=50, blank=False)
    origin_state = models.CharField(max_length=50, default="N/A", blank=False)
    destination = models.CharField(max_length=50, blank=False)
    destination_state = models.CharField(max_length=50, default="N/A", blank=False)
    departure_date = models.DateField(blank=False)
    passenger_list = models.ManyToManyField(User, blank=True)
    asking_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=5, validators=[MinValueValidator(Decimal('0.01'))])
    seats_available = models.IntegerField(default=0, choices = [(i,i) for i in range(1,6)])
    created_rides = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_rides", null=True)

    @property
    def has_not_passed(self):
        return self.departure_date >= date.today()
    def alter_seats_available_on_join(self):
        if self.seats_available > 0:
            self.seats_available -= 1
    def alter_seats_available_on_leave(self):
        self.seats_available += 1
    def set_price(self, price):
        self.asking_price = price

    # seats_available = models.PositiveIntegerField(choices = [(i,i) for i in range(1,6)], validators=[MinValueValidator(0), MaxValueValidator(6)])
    def __str__(self):
        return '%s %s %s' % (self.origin, self.destination, self.departure_date)


class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, on_delete=models.CASCADE)#, null=False, db_index=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250, blank=True, null=True)
    hometown = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    rides = models.ManyToManyField(Ride, db_index=True, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    car = models.CharField(max_length = 30, blank=True,null=True)
    def __str__(self):
        return '%s' % (self.user)
    # @property
    # def phone_number_display(self):
    #     return "$%s" % self.phone_number



#was having an issue where first time users couldnt log in OR returning users couldnt log in -- might be fixed?
#if logging in locally, comment out the "if" condition and login, then uncomment it and it should work fine
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()