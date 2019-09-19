from django.contrib import admin
from . models import Garage,Car

class GarageAdmin(admin.ModelAdmin):
    pass

class CarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Garage)
admin.site.register(Car)