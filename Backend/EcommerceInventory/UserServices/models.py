from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    name = models.CharField(max_length=100 , null=True , blank=True) 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15 , null=True , blank=True)
    address = models.TextField(null=True , blank=True)
    city = models.CharField(max_length=50 , null=True , blank=True)
    state = models.CharField(max_length=50 , null=True , blank=True)
    country = models.CharField(max_length=50 , null=True , blank=True , choices=[('India','India'),('USA','USA'),('UK','UK'),('Australia','Australia') , ('Canada','Canada') , ('Malaysia','Malaysia') , ('Singapore','Singapore'), ('UAE','UAE')])
    pincode = models.CharField(max_length=10 , null=True , blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/' , null=True , blank=True)
    account_status = models.BooleanField(default=True , null=True , blank=True , choices=[('active','active'),('inactive','inactive'),('blocked','blocked')])
    role = models.CharField(max_length=50 , null=True , blank=True , choices=[('admin','admin'),('user','user') , ('supplier','supplier') , ('customer','customer') , ('staff','staff') , ('manager','manager')])
    dob = models.DateField(null=True , blank=True)
    username = models.CharField(max_length=50 , null=True , blank=True)
    passowrd = models.CharField(max_length=50 , null=True , blank=True)
    social_media_links = models.TextField(null=True , blank=True)
    additional_details = models.JSONField(null=True , blank=True)
    language = models.CharField(max_length=50 , null=True , blank=True , choices=[('English','English'),('Hindi','Hindi'), ('Tamil','Tamil') , ('Telugu','Telugu') , ('Kannada','Kannada') , ('Malayalam','Malayalam') , ('Gujarati','Gujarati') , ('Marathi','Marathi') , ('Bengali','Bengali') , ('Punjabi','Punjabi') , ('Odia','Odia') , ('Urdu','Urdu') , ('Sanskrit','Sanskrit')])
    department = models.CharField(max_length=50 , null=True , blank=True , choices=[('IT','IT'),('HR','HR'),('Finance','Finance') , ('Sales','Sales') , ('Marketing','Marketing') , ('Production','Production') , ('Quality','Quality') , ('Purchase','Purchase') , ('Logistics','Logistics') , ('Admin','Admin') , ('Security','Security') , ('Legal','Legal') , ('R&D','R&D') , ('Maintenance','Maintenance') , ('Service','Service') , ('Support','Support') , ('Training','Training') , ('Consulting','Consulting') , ('Operations','Operations') , ('Management','Management') , ('Others','Others')])
    designation = models.CharField(max_length=50 , null=True , blank=True , choices=[('CEO','CEO'),('CFO','CFO'),('CTO','CTO') , ('CMO','CMO') , ('COO','COO') , ('CIO','CIO') , ('CDO','CDO') , ('CRO','CRO') , ('CISO','CISO') , ('CSO','CSO') , ('CPO','CPO') , ('CLO','CLO') , ('CBO','CBO') , ('CVO','CVO') , ('CQO','CQO') , ('CLO','CLO') , ('CDO','CDO') , ('CNO','CNO')])
    time_zone = models.CharField(max_length=50 , null=True , blank=True , choices = [('IST','IST'),('EST','EST'),('PST','PST'),('CST','CST'),('MST','MST'),('PST','PST'),('GMT','GMT'),('CET','CET'),('EET','EET'),('SGT','SGT'),('MYT','MYT'),('AET','AET'),('NZT','NZT')])
    last_login = models.DateTimeField(auto_now=True)
    last_device = models.CharField(max_length=50 , null=True , blank=True)
    last_ip = models.GenericIPAddressField(null=True , blank=True)
    currency = models.CharField(max_length=50 , null=True , blank=True , choices=[('USD','USD'),('INR','INR'),('EUR','EUR'),('GBP','GBP'),('AUD','AUD'),('CAD','CAD'),('SGD','SGD'),('MYR','MYR'),('AED','AED'),('NZD','NZD')])
    domain_user_id = models.CharField(max_length=50 , null=True , blank=True)
    domain_name = models.CharField(max_length=50 , null=True , blank=True)
    plan_type = models.CharField(max_length=50 , null=True , blank=True , choices=[('free','free'),('basic','basic'),('standard','standard'),('premium','premium'),('enterprise','enterprise')])
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class UserShippingAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users , on_delete=models.CASCADE , null=True , blank=True)
    name = models.CharField(max_length=50 , null=True , blank=True)
    address = models.TextField(null=True , blank=True)
    address_type = models.CharField(max_length=50 , null=True , blank=True , choices=[('home','home'),('office','office'),('other','other')])
    city = models.CharField(max_length=50 , null=True , blank=True)
    state = models.CharField(max_length=50 , null=True , blank=True)
    pincode = models.CharField(max_length=10 , null=True , blank=True)
    country = models.CharField(max_length=50 , null=True , blank=True , choices=[('India','India'),('USA','USA'),('UK','UK'),('Australia','Australia') , ('Canada','Canada') , ('Malaysia','Malaysia') , ('Singapore','Singapore'), ('UAE','UAE')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class Modules(models.Model):
    id = models.AutoField(primary_key=True)
    module_icon = models.CharField(max_length=50 , null=True , blank=True)
    module_name = models.CharField(max_length=50 , null=True , blank=True)
    is_active = models.BooleanField(default=True , null=True , blank=True)
    is_menu = models.BooleanField(default=True , null=True , blank=True)
    parent_id = models.ForeignKey('self' , on_delete=models.CASCADE , null=True , blank=True)
    module_description = models.TextField(null=True , blank=True)
    module_url = models.CharField(max_length=100 , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class UserPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users , on_delete=models.CASCADE , null=True , blank=True)
    module = models.ForeignKey(Modules , on_delete=models.CASCADE , null=True , blank=True)
    is_view = models.BooleanField(default=True , null=True , blank=True)
    is_add = models.BooleanField(default=True , null=True , blank=True)
    is_edit = models.BooleanField(default=True , null=True , blank=True)
    is_delete = models.BooleanField(default=True , null=True , blank=True)
    domain_user_id = models.CharField(max_length=50 , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class ActivityLog(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users , on_delete=models.CASCADE , null=True , blank=True)
    activity = models.TextField(null=True , blank=True)
    activity_type = models.CharField(max_length=50 , null=True , blank=True)
    activity_date = models.DateTimeField(auto_now_add=True)
    activity_ip = models.GenericIPAddressField(null=True , blank=True)
    activity_device = models.CharField(max_length=50 , null=True , blank=True)
    domain_user_id = models.CharField(max_length=50 , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)