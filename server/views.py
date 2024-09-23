from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .serializers import *
from .models import *
# Create your views here.

class RoomAPIView(ListAPIView,CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

class TenantAPIView(ListAPIView,CreateAPIView):
    queryset =Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes =[AllowAny]
class officesAPIView(ListAPIView,CreateAPIView):
    queryset=offices.objects.all()
    serializer_class= officesSerializer
    permission_classes =[AllowAny]
class ShopsAPIView(ListAPIView,CreateAPIView):
    queryset= Shops.objects.all()
    serializer_class=ShopsSerializer
    permission_classes =(AllowAny)
class estatesAPIView(ListAPIView,CreateAPIView):
    queryset =estates.objects.all()
    serializer_class=estatesSerializer
    permission_classes = [AllowAny]
class godownsAPIView(ListAPIView,CreateAPIView):
    queryset = godowns.objects.all()
    serializer_class=godownsSerializer
    permission_classes =[ AllowAny]
class hotelsAPIView(ListAPIView,CreateAPIView):
    queryset =  hotels.objects.all()
    serializer_class = hotelsSerializer
    permission_classes = [AllowAny]
class BungalowAPIView(ListAPIView,CreateAPIView):
    queryset= Bungalow.objects.all()
    serializer_class= BungalowSerializer
    permission_classes= [AllowAny]
class StudentHostelsAPIView(ListAPIView,CreateAPIView):
    queryset= StudentHostels.objects.all()
    serializer_class= StudentHostelsSerializer
    permission_classes = [AllowAny]

class LadiesHostelsAPIView(ListAPIView, CreateAPIView):
    queryset=LadiesHostels.objects.all()
    serializer_class=LadiesHostelsSerializer
    permission_classes = [AllowAny]

class KioskShopsAPIView(ListAPIView, CreateAPIView):
    queryset=KioskShops.objects.all()
    serializer_class=KioskShopsSerializer
    permission_classes = [AllowAny]
