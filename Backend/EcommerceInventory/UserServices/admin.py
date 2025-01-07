from django.contrib import admin
from . models import Users, UserShippingAddress, Modules, UserPermissions, ActivityLog
# Register your models here.
admin.site.register(Users)
admin.site.register(UserShippingAddress)
admin.site.register(Modules)
admin.site.register(UserPermissions)
admin.site.register(ActivityLog)