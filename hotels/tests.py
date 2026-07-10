from django.test import TestCase
from .models import Hotel

class HotelModelTest(TestCase):
    def test_str(self):
        hotel = Hotel(name="Hilton", city="Tokyo")
        self.assertEqual(str(hotel), "Hilton")