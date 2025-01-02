from django.db import models
from OrderServices.models import PurchaseOrder, PurchaseOrderItemInwardedLog, PurchaseOrderItems, SalesOrder
from ProductServices.models import Products
from UserServices.models import Users
# Create your models here.


class Warehouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , null=True , blank=True)
    address = models.TextField()
    city = models.CharField(max_length=50 , null=True , blank=True)
    state = models.CharField(max_length=50 , null=True , blank=True)
    country = models.CharField(max_length=50 , null=True , blank=True)
    pincode = models.CharField(max_length=50 , null=True , blank=True)
    warehouse_manger = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='warehouse_manger')
    phone = models.CharField(max_length=50 , null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    status = models.CharField(max_length=50 , null=True , blank=True , choices=[('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE')])
    size = models.CharField(max_length=50 , null=True , blank=True , choices=[('SMALL','SMALL'),('MEDIUM','MEDIUM'),('LARGE','LARGE')])
    capacity = models.CharField(max_length=50 , null=True , blank=True , choices=[('SMALL','SMALL'),('MEDIUM','MEDIUM'),('LARGE','LARGE')])
    warehouse_type = models.CharField(max_length=50 , null=True , blank=True , choices=[('OWNED','OWNED'),('LEASED','LEASED')])
    additional_details = models.JSONField(null=True , blank=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='domain_user_id')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='added_by_user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

class RackAndShelvesAndFloor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , null=True , blank=True)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE , null=True , blank=True)
    rack = models.CharField(max_length=50 , null=True , blank=True)
    shelf = models.CharField(max_length=50 , null=True , blank=True)
    floor = models.CharField(max_length=50 , null=True , blank=True)
    additional_details = models.JSONField(null=True , blank=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='rack_domain_user_id')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='rack_added_by_user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_order_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE , null=True , blank=True)
    purchase_order_item_id = models.ForeignKey(PurchaseOrderItems, on_delete=models.CASCADE , null=True , blank=True)
    purchase_order_item_inwarded_item_id = models.ForeignKey(PurchaseOrderItemInwardedLog, on_delete=models.CASCADE , null=True , blank=True , related_name='purchase_order_item_inwarded_item_id')
    product_id = models.ForeignKey(Products , on_delete=models.CASCADE , null=True , blank=True)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE , null=True , blank=True)
    rack_shelf_floor_id = models.ForeignKey(RackAndShelvesAndFloor, on_delete=models.CASCADE , null=True , blank=True)
    quantity = models.IntegerField() 
    mrp = models.CharField (max_length=50 , null=True , blank=True)
    batch_number = models.CharField(max_length=50 , null=True , blank=True)
    discount_type = models.CharField(max_length=50 , null=True , blank=True , choices=[('PERCENTAGE','PERCENTAGE'),('AMOUNT','AMOUNT')])
    discount_value = models.CharField(max_length=50 , null=True , blank=True)
    discount_amount = models.CharField(max_length=50 , null=True , blank=True)
    sr_no = models.CharField(max_length=50 , null=True , blank=True)
    mfg_date = models.DateField(null=True , blank=True)
    uom = models.CharField(max_length=50 , null=True , blank=True)
    ptr = models.CharField(max_length=50 , null=True , blank=True)
    recieved_date = models.DateField(null=True , blank=True)    
    expiry_date = models.DateField(null=True , blank=True)
    quqantity_inwarded = models.IntegerField()
    buy_price = models.CharField(max_length=50 , null=True , blank=True)
    sell_price = models.CharField(max_length=50 , null=True , blank=True)
    tax_percentage = models.CharField(max_length=50 , null=True , blank=True)
    stock_status = models.CharField(max_length=50 , null=True , blank=True , choices=[('IN_STOCK','IN_STOCK'),('OUT_OF_STOCK','OUT_OF_STOCK') , ('DAMAGED','DAMAGED') , ('LOST','LOST')])
    inward_type = models.CharField(max_length=50 , null=True , blank=True , choices=[('PURCHASE','PURCHASE'),('RETURN','RETURN')])
    addititon_details = models.JSONField(null=True , blank=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='inventory_domain_user_id')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='inventory_added_by_user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class InventryLog(models.Model):
    id = models.AutoField(primary_key=True)
    po_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE , null=True , blank=True)
    so_id = models.ForeignKey(SalesOrder, on_delete=models.CASCADE , null=True , blank=True , related_name='so_id')
    inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE , null=True , blank=True)
    Warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE , null=True , blank=True)
    rack_shelf_floor_id = models.ForeignKey(RackAndShelvesAndFloor, on_delete=models.CASCADE , null=True , blank=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50 , null=True , blank=True , choices=[('INWARD','INWARD'),('OUTWARD','OUTWARD') , ('DAMAGED','DAMAGED') , ('LOST','LOST') , ('EXPIRED','EXPIRED') , ('RETURN','RETURN') , ('ADJUSTMENT','ADJUSTMENT') , ('WAREHOUSE TRANSFER','WAREHOUSE TRANSFER')])
    additional_details = models.JSONField(null=True , blank=True)#
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='inventry_log_domain_user_id')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='inventry_log_added_by_user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    