from django.test import TestCase

from django.test import TestCase
from rides.models import Ride
from rides.models import User
import datetime
# Create your tests here.

class TestCases(TestCase):
    def setUp(self):
        Ride.objects.create(origin="Charlottesville", destination="Blacksburg", departure_date="2019-10-10", seats_available=4)
        Ride.objects.create(origin="Blacksburg", destination="Washington DC", departure_date="2019-10-20", seats_available=0)
        Ride.objects.create(origin="Virginia Beach", destination="Norfolk", departure_date="2019-10-30", seats_available=1000)

        # User.objects.create(first_name="John", last_name="Doe", email="jd3aa@virginia.edu")
        # User.objects.create(first_name="Jane", last_name="Deer", email="jd4ab@virginia.edu")
        # User.objects.create(first_name="Mark", last_name="Sherrif", email="mark@virginia.edu")

    # def test_user_name(self):
    #     john = User.objects.get(first_name="John")
    #     jane = User.objects.get(first_name="Jane")
    #     mark = User.objects.get(first_name="Mark")
    #
    #     self.assertEqual(john.last_name, "Doe")
    #     self.assertEqual(jane.last_name, "Deer")
    #     self.assertEqual(mark.last_name, "Sherrif")
    #
    #     self.assertEqual(john.first_name, "John")
    #     self.assertEqual(jane.first_name, "Jane")
    #     self.assertEqual(mark.first_name, "Mark")
    #
    # def test_user_email(self):
    #     john = User.objects.get(first_name="John")
    #     jane = User.objects.get(first_name="Jane")
    #     mark = User.objects.get(first_name="Mark")
    #
    #     self.assertEqual(john.email, "jd3aa@virginia.edu")
    #     self.assertEqual(jane.email, "jd4ab@virginia.edu")
    #     self.assertEqual(mark.email, "mark@virginia.edu")
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

    def test_year(self):
        cville = Ride.objects.get(origin="Charlottesville")
        vb757 = Ride.objects.get(origin="Virginia Beach")
        blacksburg = Ride.objects.get(origin="Blacksburg")

        self.assertEqual(cville.departure_date.strftime("%Y"), "2019")
        self.assertEqual(blacksburg.departure_date.strftime("%Y"), "2019")
        self.assertEqual(vb757.departure_date.strftime("%Y"), "2019")

    def test_month(self):
        cville = Ride.objects.get(origin="Charlottesville")
        vb757 = Ride.objects.get(origin="Virginia Beach")
        blacksburg = Ride.objects.get(origin="Blacksburg")

        self.assertEqual(cville.departure_date.strftime("%m"), "10")
        self.assertEqual(blacksburg.departure_date.strftime("%m"), "10")
        self.assertEqual(vb757.departure_date.strftime("%m"), "10")

    def test_day(self):
        cville = Ride.objects.get(origin="Charlottesville")
        vb757 = Ride.objects.get(origin="Virginia Beach")
        blacksburg = Ride.objects.get(origin="Blacksburg")

        self.assertEqual(cville.departure_date.strftime("%d"), "10")
        self.assertEqual(blacksburg.departure_date.strftime("%d"), "20")
        self.assertEqual(vb757.departure_date.strftime("%d"), "30")

    def test_date_type(self):
        cville = Ride.objects.get(origin="Charlottesville")
        vb757 = Ride.objects.get(origin="Virginia Beach")
        blacksburg = Ride.objects.get(origin="Blacksburg")

        self.assertEqual(type(cville.departure_date), type(datetime.date(2019, 10, 10)))
        self.assertEqual(type(blacksburg.departure_date), type(datetime.date(2019, 10, 10)))
        self.assertEqual(type(vb757.departure_date), type(datetime.date(2019, 10, 10)))

    def test_dummy_test_case(self):
        self.assertEqual(1, 1)