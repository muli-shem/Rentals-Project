from django.urls import  path
from .views import *

urlpatterns = [
    path("room/" ,RoomAPIView.as_view(), name="create-room"), # Create a room
    path("tenant" ,TenantAPIView.as_view(),name ="tenant"),
]