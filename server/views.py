from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .seriallizer import *
from .models import *
# Create your views here.

class RoomAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

class TenantAPIView(ListAPIView):
    queryset =Room.objects.all()
    serializer_class = TenantSerializer
    permission_classes =[AllowAny]
