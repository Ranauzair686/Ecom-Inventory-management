from django.db import models
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
    domain_user_id = models.ForeignKey('UserServices.Users', on_delete=models.CASCADE , null=True , blank=True , related_name='domain_user_id')
    added_by_user_id = models.ForeignKey('UserServices.Users', on_delete=models.CASCADE , null=True , blank=True , related_name='added_by_user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)