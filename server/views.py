from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .serializers import *
from .models import *
# Create your views here.

class RoomAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

class TenantAPIView(ListAPIView):
    queryset =Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes =[AllowAny]
class officesAPIView(ListAPIView):
    queryset=offices.objects.all()
    serializer_class= officesSerializer
    permission_classes =[AllowAny]
class ShopsAPIView(ListAPIView):
    queryset= Shops.objects.all()
    serializer_class=ShopsSerializer
    permission_classes =(AllowAny)
class estatesAPIView(ListAPIView):
    queryset =estates.objects.all()
    serializer_class=estatesSerializer
    permission_classes = [AllowAny]
class godownsAPIView(ListAPIView):
    queryset = godowns.objects.all()
    serializer_class=godownsSerializer
    permission_classes =[ AllowAny]
class hotelsAPIView(ListAPIView):
    queryset =  hotels.objects.all()
    serializer_class = hotelsSerializer
    permission_classes = [AllowAny]



    