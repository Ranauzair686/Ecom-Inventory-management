from django.db import models
from InventoryServices.models import Warehouse
from UserServices.models import Users

# Create your models here.


class PurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse_id = models.ForeignKey(Warehouse , on_delete=models.CASCADE ,related_name='warehouse_id')
    supplier_id = models.ForeignKey(Users , on_delete=models.CASCADE , related_name='supplier_id')
    last_updateb_by_user_id = models.ForeignKey(Users , on_delete=models.CASCADE , related_name='last_updateb_by_user_id')
    po_code = models.CharField(max_length=50 , null=True , blank=True)
    po_date = models.DateField(null=True , blank=True)
    expected_delivery_date = models.DateField(null=True , blank=True)
    payment_terms = models.CharField(max_length=50 , null=True , blank=True , choices=[('credit','credit'),('cash','cash'),('cheque','cheque'),('online','online')])
    payment_status = models.CharField(max_length=50 , null=True , blank=True , choices=[('paid','paid'),('unpaid','unpaid'),('partial paid','partial paid') , ('advance','advance'), ('cancelled','cancelled')])
    total_amount = models.FloatField(null=True , blank=True)
    paid_amount = models.FloatField(null=True , blank=True)
    due_amount = models.FloatField(null=True , blank=True)
    discount_amount = models.FloatField(null=True , blank=True)
    discount_type = models.CharField(max_length=50 , null=True , blank=True , choices=[('percentage','percentage'),('fixed','fixed')])
    shipping_amount = models.FloatField(null=True , blank=True)
    shipping_type = models.CharField(max_length=50 , null=True , blank=True , choices=[('free','free'),('paid','paid')])
    shipping_tax = models.FloatField(null=True , blank=True)
    status = models.CharField(max_length=50 , null=True , blank=True , choices=[('draft','draft'),('confirmed','confirmed'),('shipped','shipped'),('delivered','delivered'),('cancelled','cancelled')])