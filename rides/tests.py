from django.test import TestCase

from django.test import TestCase
from rides.models import Ride
from rides.models import Profile
# from rides.models import User
import datetime
# Create your tests here.

class TestCases(TestCase):
    def setUp(self):
        Ride.objects.create(origin="Charlottesville", destination="Blacksburg", departure_date="2019-10-10", seats_available=4)
        Ride.objects.create(origin="Blacksburg", destination="Washington DC", departure_date="2019-10-20", seats_available=0)
        Ride.objects.create(origin="Virginia Beach", destination="Norfolk", departure_date="2019-10-30", seats_available=1000)
        Ride.objects.create(origin="Indianapolis, IN", destination="Denver, CO", departure_date="2019-11-12", seats_available=-1)

        # Profile.objects.create(bio="I am a new user", location="Charlottesville, VA")
        # Profile.objects.create(bio="I am another user", location="Blacksburg, VA")
        # Profile.objects.create(bio="I am a third user", location="Indianapolis, IN")


    def test_destination_cho(self):
        cville = Ride.objects.get(origin="Charlottesville")
        self.assertEqual(cville.destination, "Blacksburg")

    def test_destination_vb(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        self.assertEqual(vb757.destination, "Norfolk")

    def test_destination_b(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        self.assertEqual(blacksburg.destination, "Washington DC")

    def test_join_cho(self):
        cville = Ride.objects.get(origin="Charlottesville")
        cville.alter_seats_available_on_join()
        self.assertEqual(cville.seats_available, 3)
    def test_leave_cho(self):
        cville = Ride.objects.get(origin="Charlottesville")
        cville.alter_seats_available_on_leave()
        self.assertEqual(cville.seats_available, 5)
    def test_join_b(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        blacksburg.alter_seats_available_on_join()
        self.assertEqual(blacksburg.seats_available, 0)
    def test_leave_b(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        blacksburg.alter_seats_available_on_leave()
        self.assertEqual(blacksburg.seats_available, 1)
    def test_leave_vb(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        vb757.alter_seats_available_on_leave()
        self.assertEqual(vb757.seats_available, 1001)
    def test_join_vb(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        vb757.alter_seats_available_on_join()
        self.assertEqual(vb757.seats_available, 999)
    def test_leave_ind(self):
        indy = Ride.objects.get(origin="Indianapolis, IN")
        indy.alter_seats_available_on_leave()
        self.assertEqual(indy.seats_available, 0)
    def test_join_ind(self):
        indy = Ride.objects.get(origin="Indianapolis, IN")
        indy.alter_seats_available_on_join()
        self.assertEqual(indy.seats_available, -1)


    def test_seats_available_cho(self):
        cville = Ride.objects.get(origin="Charlottesville")
        self.assertEqual(cville.seats_available, 4)

    def test_seats_available_vb(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        self.assertEqual(vb757.seats_available, 1000)
    def test_seats_available_b(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        self.assertEqual(blacksburg.seats_available, 0)
    def test_seats_available_in(self):
        indy = Ride.objects.get(origin="Indianapolis, IN")
        self.assertEqual(indy.seats_available, -1)




    def test_year_cho(self):
        cville = Ride.objects.get(origin="Charlottesville")
        self.assertEqual(cville.departure_date.strftime("%Y"), "2019")
    def test_year_vb(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        self.assertEqual(vb757.departure_date.strftime("%Y"), "2019")
    def test_year_b(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        self.assertEqual(blacksburg.departure_date.strftime("%Y"), "2019")



    def test_month1(self):
        cville = Ride.objects.get(origin="Charlottesville")
        self.assertEqual(cville.departure_date.strftime("%m"), "10")
    def test_month2(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        self.assertEqual(vb757.departure_date.strftime("%m"), "10")
    def test_month3(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        self.assertEqual(blacksburg.departure_date.strftime("%m"), "10")



    def test_day_cho(self):
        cville = Ride.objects.get(origin="Charlottesville")
        self.assertEqual(cville.departure_date.strftime("%d"), "10")
    def test_day_vb(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        self.assertEqual(vb757.departure_date.strftime("%d"), "30")
    def test_day_b(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        self.assertEqual(blacksburg.departure_date.strftime("%d"), "20")



    def test_date_type_cho(self):
        cville = Ride.objects.get(origin="Charlottesville")
        self.assertEqual(type(cville.departure_date), type(datetime.date(2019, 10, 10)))
    def test_data_type_vb(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        self.assertEqual(type(vb757.departure_date), type(datetime.date(2019, 10, 10)))
    def test_data_type_b(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        self.assertEqual(type(blacksburg.departure_date), type(datetime.date(2019, 10, 10)))



    def test_id_pk1(self):
        cville = Ride.objects.get(origin="Charlottesville")
        blacksburg = Ride.objects.get(origin="Blacksburg")
        self.assertNotEqual(cville.id, blacksburg.id)
    def test_id_pk2(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        vb757 = Ride.objects.get(origin="Virginia Beach")
        self.assertNotEqual(vb757.id, blacksburg.id)
    def test_id_pk3(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        cville = Ride.objects.get(origin="Charlottesville")
        self.assertNotEqual(cville.id, vb757.id)


    # def test_profile_bio(self):
    #     user1 = User.objects.get(location="Charlottesville, VA")
    #     user2 = User.objects.get(location="Indianapolis, IN")
    #     self.assertNotEqual(user1.bio, user2.bio)


