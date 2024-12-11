from django.test import TestCase
from ..models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        menu_item = Menu.objects.create(title='Ice Cream', price=80, inventory=100)
        self.assertEqual(str(menu_item), 'Ice Cream : 80')
        
        
class BookingTest(TestCase):
    def test_get_item(self):
        booking_item = Booking.objects.create(name='John', no_of_guests=4, bookingDate='2022-01-01')
        self.assertEqual(str(booking_item), 'John')
        
    def test_no_of_guests_validation(self):
            with self.assertRaises('ValidationError'):
                Booking.objects.create(name='John', no_of_guests=-1, bookingDate='2022-01-01')

    def test_booking_date_validation(self):
            with self.assertRaises('ValidationError'):
                Booking.objects.create(name='John', no_of_guests=4, bookingDate=' invalid-date ')