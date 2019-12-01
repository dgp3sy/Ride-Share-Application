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
        Ride.objects.create(origin="Blacksburg", destination="Washington DC", departure_date="2019-10-20", asking_price=0, seats_available=0)
        Ride.objects.create(origin="Virginia Beach", destination="Norfolk", departure_date="2019-10-30", seats_available=1000)
        Ride.objects.create(origin="Indianapolis, IN", destination="Denver, CO", departure_date="2019-11-12", seats_available=-1)

        Ride.objects.create(origin="Richmond", origin_state="Virginia", destination="Santa Fe", destination_state="New Mexico",
                            departure_date="2019-10-10", seats_available=4, asking_price=20.00)
        Ride.objects.create(origin="Seattle", origin_state="Washington", destination="Des Moines",
                            destination_state="Iowa",
                            departure_date="2019-10-10", seats_available=4, asking_price=200)
        Ride.objects.create(origin="Chicago", origin_state="Illinois", destination="Phoenix",
                            destination_state="Arizona",
                            departure_date="2019-10-10", seats_available=4, asking_price=2.001)


######### DESTINATION STATE ############
    def test_state_dest_NM(self):
        ride = Ride.objects.get(origin="Richmond")
        self.assertEqual("New Mexico", ride.destination_state)
    def test_state_dest_IA(self):
        ride = Ride.objects.get(origin="Seattle")
        self.assertEqual("Iowa", ride.destination_state)
    def test_state_dest_AZ(self):
        ride = Ride.objects.get(origin="Chicago")
        self.assertEqual("Arizona", ride.destination_state)
    def test_state_origin_NA1(self):
        ride = Ride.objects.get(origin="Virginia Beach")
        self.assertEqual("N/A", ride.destination_state)
    def test_state_origin_NA2(self):
        ride = Ride.objects.get(origin="Charlottesville")
        self.assertEqual("N/A", ride.destination_state)
    def test_state_origin_NA3(self):
        ride = Ride.objects.get(origin="Blacksburg")
        self.assertEqual("N/A", ride.destination_state)

    ######### ORIGIN STATE ############

    def test_state_origin_VA(self):
        ride = Ride.objects.get(origin="Richmond")
        self.assertEqual("Virginia", ride.origin_state)
    def test_state_origin_WA(self):
        ride = Ride.objects.get(origin="Seattle")
        self.assertEqual("Washington", ride.origin_state)
    def test_state_origin_IL(self):
        ride = Ride.objects.get(origin="Chicago")
        self.assertEqual("Illinois", ride.origin_state)
    def test_state_origin_NA1(self):
        ride = Ride.objects.get(origin="Virginia Beach")
        self.assertEqual("N/A", ride.origin_state)
    def test_state_origin_NA2(self):
        ride = Ride.objects.get(origin="Charlottesville")
        self.assertEqual("N/A", ride.origin_state)
    def test_state_origin_NA3(self):
        ride = Ride.objects.get(origin="Blacksburg")
        self.assertEqual("N/A", ride.origin_state)

    ######### PRICE ############

    def set_price_vb(self):
        ride = Ride.objects.get(origin="Virginia Beach")
        self.assertRaises(ride.set_price("potato"))
    def test_price_cho(self):
        ride = Ride.objects.get(origin="Charlottesville")
        self.assertEqual(ride.asking_price, 0.00)
    def test_price_b(self):
        ride = Ride.objects.get(origin="Blacksburg")
        self.assertEqual(ride.asking_price, 0)
    def test_price_richmond(self):
        ride = Ride.objects.get(origin="Richmond")
        self.assertEqual(ride.asking_price, 20.00)
    def test_price_seattle(self):
        ride = Ride.objects.get(origin="Seattle")
        self.assertEqual(ride.asking_price, 200)
    def test_price_chicago(self):
        ride = Ride.objects.get(origin="Chicago")
        self.assertEqual(ride.asking_price, 2.00)
    def set_price_chicago(self):
        ride = Ride.objects.get(origin="Chicago")
        ride.set_price(40)
        self.assertEqual(ride.asking_price, 40.00)

    ######### DESTINATION CITY ############

    def test_destination_cho(self):
        cville = Ride.objects.get(origin="Charlottesville")
        self.assertEqual(cville.destination, "Blacksburg")
    def test_destination_vb(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        self.assertEqual(vb757.destination, "Norfolk")
    def test_destination_b(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        self.assertEqual(blacksburg.destination, "Washington DC")
    def test_destination_rich(self):
        cville = Ride.objects.get(origin="Richmond")
        self.assertEqual(cville.destination, "Santa Fe")
    def test_destination_seattle(self):
        cville = Ride.objects.get(origin="Seattle")
        self.assertEqual(cville.destination, "Des Moines")
    def test_destination_chi(self):
        cville = Ride.objects.get(origin="Chicago")
        self.assertEqual(cville.destination, "Phoenix")

    ######### JOINING RIDES ############

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

    ######### SEATS AVAILABLE ############

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

    ######### DATE ############
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

    ######### DATE TYPE ############
    def test_date_type_cho(self):
        cville = Ride.objects.get(origin="Charlottesville")
        self.assertEqual(type(cville.departure_date), type(datetime.date(2019, 10, 10)))
    def test_data_type_vb(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        self.assertEqual(type(vb757.departure_date), type(datetime.date(2019, 10, 10)))
    def test_data_type_b(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        self.assertEqual(type(blacksburg.departure_date), type(datetime.date(2019, 10, 10)))

    ######### ID AS PRIMARY KEY ############
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
    def test_id_pk4(self):
        Ride.objects.create(origin="Norfolk", origin_state="Virginia", destination="Crozet", destination_state="Virginia",
                            departure_date="2019-10-10", seats_available=4, asking_price=20.00)
        new_ride = Ride.objects.get(origin="Norfolk")
        vb757 = Ride.objects.get(origin="Virginia Beach")
        cville = Ride.objects.get(origin="Charlottesville")
        blacksburg = Ride.objects.get(origin="Blacksburg")
        self.assertNotEqual(new_ride.id, vb757.id)
        self.assertNotEqual(new_ride.id, cville.id)
        self.assertNotEqual(new_ride.id, blacksburg.id)
    def test_id_pk5(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        cville = Ride.objects.get(origin="Charlottesville")
        blacksburg = Ride.objects.get(origin="Blacksburg")

        Ride.objects.create(origin="Norfolk", origin_state="Virginia", destination="Crozet", destination_state="Virginia",
                            departure_date="2019-10-10", seats_available=4, asking_price=20.00)

        Ride.objects.get(origin="Norfolk").delete()
        self.assertNotEqual(vb757.id, cville.id)
        self.assertNotEqual(blacksburg.id, cville.id)
        self.assertNotEqual(vb757.id, blacksburg.id)



    ####### CHANGES TO DESTINATION #######
    def test_delta_destination_cho(self):
        cville = Ride.objects.get(origin="Charlottesville")
        cville.destination="Norfolk"
        self.assertEqual(cville.destination, "Norfolk")
    def test_delta_destination_vb(self):
        vb757 = Ride.objects.get(origin="Virginia Beach")
        vb757.destination="Alexandria"
        self.assertEqual(vb757.destination, "Alexandria")
    def test_delta_destination_b(self):
        blacksburg = Ride.objects.get(origin="Blacksburg")
        blacksburg.destination="Hampton Roads"
        self.assertEqual(blacksburg.destination, "Hampton Roads")
    def test_delta_destination_rich(self):
        ride = Ride.objects.get(origin="Richmond")
        ride.destination="Raton"
        self.assertEqual(ride.destination, "Raton")
    def test_delta_destination_seattle(self):
        ride = Ride.objects.get(origin="Seattle")
        ride.destination="Mount Pleasant"
        self.assertEqual(ride.destination, "Mount Pleasant")
    def test_delta_destination_chi(self):
        ride = Ride.objects.get(origin="Chicago")
        ride.destination="Springfield"
        self.assertEqual(ride.destination, "Springfield")


    def test_delta_destination_state_rich(self):
        ride = Ride.objects.get(origin="Richmond")
        ride.destination_state="California"
        self.assertEqual(ride.destination, "Santa Fe")
        self.assertEqual(ride.destination_state, "California")
    def test_delta_destination_seattle(self):
        ride = Ride.objects.get(origin="Seattle")
        ride.destination_state="Idaho"
        self.assertEqual(ride.destination, "Des Moines")
        self.assertEqual(ride.destination_state, "Idaho")
    def test_delta_destination_state_chi(self):
        ride = Ride.objects.get(origin="Chicago")
        ride.destination_state="Missouri"
        self.assertEqual(ride.destination, "Phoenix")
        self.assertEqual(ride.destination_state, "Missouri")
