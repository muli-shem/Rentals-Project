from django.urls import  path
from .views import *

urlpatterns = [
    path("room/" ,RoomAPIView.as_view(), name="create-room"),
    path("tenant/" ,TenantAPIView.as_view(), name ="tenant"),
    path("shops/",ShopsAPIView.as_view(),name='shop'),
    path("offices/",officesAPIView.as_view(),name='office'),
    path("godowns/",godownsAPIView.as_view(),name="godown"),
    path("hotels/",hotelsAPIView.as_view() ,name="add-hotel"),
    path("estates/",estatesAPIView.as_view() ,name="add-estate"),
    path("Bungalow/",BungalowAPIView.as_view(),name="Bungalow")
    
]