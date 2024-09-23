from django.contrib import admin
from .models import Room,Tenant,estates,Shops,offices,godowns,hotels,Bungalow,StudentHostels,LadiesHostels,KioskShops
admin.site.register(Room)
admin.site.register(Tenant)
admin.site.register(estates)
admin.site.register(Shops)
admin.site.register(offices)
admin.site.register(godowns)
admin.site.register(hotels)
admin.site.register(Bungalow)
admin.site.register(StudentHostels)
admin.site.register(LadiesHostels)

class KioskShopsAdmin(admin.ModelAdmin):
    list_display = ('County', 'Street', 'location', 'owner', 'contact', 'image')
    search_fields = ('owner', 'County', 'location')

admin.site.register(KioskShops, KioskShopsAdmin)