from django.contrib import admin

# Register your models here.
from . models import Inventory , RackAndShelvesAndFloor, Warehouse , InventryLog

admin.site.register(Inventory)
admin.site.register(RackAndShelvesAndFloor)
admin.site.register(Warehouse)
admin.site.register(InventryLog)

