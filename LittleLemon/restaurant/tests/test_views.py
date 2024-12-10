from django.test import TestCase
from .models import Menu
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test menu items
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Burger", price=90, inventory=75)

    def test_getall(self):
        # Get API response
        response = self.client.get(reverse('menu'))
        
        # Get data from database
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Check status code and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)