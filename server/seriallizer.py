from rest_framework import serializers
from .models import Tenant,Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields ='__all__'
        # Create a new tenant and return
class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'