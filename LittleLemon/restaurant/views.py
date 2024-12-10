from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    