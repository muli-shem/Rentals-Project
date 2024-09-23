from rest_framework import serializers
from .models import *
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class officesSerializer(serializers.ModelSerializer):
    class Meta:
        model = offices
        fields = '__all__'

class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'

class estatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = estates
        fields = '__all__'

class godownsSerializer(serializers.ModelSerializer):
    class Meta:
        model = godowns
        fields = '__all__'

class hotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotels
        fields = '__all__'
class BungalowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bungalow
        fields = '__all__'

class StudentHostelsSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentHostels
        fields = '__all__'

class LadiesHostelsSerializer(serializers.ModelSerializer):
    class Meta:
        model=LadiesHostels
        fields = '__all__'
class KioskShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model=KioskShops
        fields = '__all__'