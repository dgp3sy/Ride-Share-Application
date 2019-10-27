from django.test import TestCase

from django.test import TestCase
from rides.models import Ride
# Create your tests here.

class TestCases(TestCase):
    def setUp(self):
        Ride.objects.create(origin="Charlottesville", destination="Blacksburg", departure_date="10/4/2019", seats_available=4)
        Ride.objects.create(origin="Blacksburg", destination="Washington DC", departure_date="10/10/2019", seats_available=0)
        Ride.objects.create(origin="Virginia Beach", destination="Norfolk", departure_date="10/30/2019", seats_available=1000)

    def test_destination(self):
        cville = Ride.objects.get(origin="Charlottesville")
        vb757 = Ride.objects.get(origin="Virginia Beach")
        blacksburg = Ride.objects.get(origin="Blacksburg")

        self.assertEqual(cville.destination, "Blacksburg")
        self.assertEqual(blacksburg.destination, "Washington DC")
        self.assertEqual(vb757.destination, "Norfolk")

    def test_seats_available(self):
        cville = Ride.objects.get(origin="Charlottesville")
        vb757 = Ride.objects.get(origin="Virginia Beach")
        blacksburg = Ride.objects.get(origin="Blacksburg")


        self.assertEqual(cville.seats_available, 4)
        self.assertEqual(vb757.seats_available, 1000)
        self.assertEqual(blacksburg.seats_available, 0)



    def test_dummy_test_case(self):
        self.assertEqual(1, 1)