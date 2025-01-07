from django.contrib import admin
from . models import PurchaseOrder, PurchaseOrderItems, PurchaseOrderInwardedLog, PurchaseOrderItemInwardedLog , PurchaseOrderLogs , SalesOrder,  SalesOrderItems, SalesOrderOutwardedLog, SalesOrderLogs , SalesOrderItemOutwardedLog
# Register your models here.
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItems)
admin.site.register(PurchaseOrderInwardedLog)
admin.site.register(PurchaseOrderItemInwardedLog)
admin.site.register(PurchaseOrderLogs)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItems)
admin.site.register(SalesOrderOutwardedLog)
admin.site.register(SalesOrderLogs)
admin.site.register(SalesOrderItemOutwardedLog)