from django.db import models
from UserServices.models import Users

# Create your models here.
class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , null=True , blank=True)
    image = models.TextField()
    description = models.TextField()
    display_order = models.IntegerField(default=0)
    parent_id = models.ForeignKey('self' , on_delete=models.CASCADE , null=True , blank=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='domain_user_id')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='added_by_user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , null=True , blank=True)
    image = models.JSONField()
    description = models.TextField()
    specifications = models.JSONField()
    html_description = models.JSONField()
    highlights = models.JSONField()
    sku = models.CharField(max_length=50 )
    initial_buying_price = models.FloatField()
    initial_selling_price = models.FloatField()
    weight = models.FloatField()
    dimensions = models.CharField(max_length=50, default='0x0x0')
    uom = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    tax_perecentage = models.FloatField()
    brand = models.CharField(max_length=50)
    brand_model = models.CharField(max_length=50)
    status = models.CharField(max_length=50 , choices=[('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE')], default='ACTIVE')
    seo_title = models.CharField(max_length=50)
    seo_description = models.CharField(max_length=50)
    seo_keywords = models.JSONField()
    additional_details = models.JSONField()
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE , null=True , blank=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='domain_user_id')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='added_by_user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
class ProductQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE , null=True , blank=True)
    question = models.TextField()
    answer = models.TextField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='domain_user_id')
    question_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='question_user_id')
    answer_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='added_by_user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=50 , choices=[('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE')], default='ACTIVE')
    
    
class ProductReviews(models.Model):
    id = models.AutoField(primary_key=True)
    review_images = models.JSONField()
    rating = models.FloatField()
    review = models.TextField()
    status = models.CharField(max_length=50 , choices=[('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE')], default='ACTIVE')
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE , null=True , blank=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='domain_user_id')
    review_user_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True , blank=True , related_name='added_by_user_id')
