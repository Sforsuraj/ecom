from typing import Any
from django.db import models
from django.contrib.auth.models import User
import os

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.category_name}_{instance.id}.{ext}"
    return os.path.join('category', filename)
class category(models.Model):
    category_name=models.CharField(max_length=100)
    category_img=models.ImageField(upload_to=content_file_name,default='')
    def __str__(self):
        return self.category_name

# Create your models here.

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.category_id.id}_{instance.id}.{ext}"
    return os.path.join('shop', filename)

class shop(models.Model):
    category_id=models.ForeignKey(category,default='', on_delete=models.CASCADE)
    product_img=models.ImageField(upload_to=content_file_name)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_discount=models.IntegerField()
    product_rating=models.IntegerField()
    
    
    def __str__(self):
        return self.product_name




    
class shop_detail(models.Model):
    product_id=models.ForeignKey(shop,default='', on_delete=models.CASCADE)
    product_short_desc=models.CharField(max_length=200)
    product_description=models.TextField(blank=True)
    product_information=models.TextField(blank=True)
    

class user_review(models.Model):
    user_id=models.ForeignKey(User,default='', on_delete=models.CASCADE)
    product_id=models.ForeignKey(shop, on_delete=models.CASCADE)
    user_rating=models.IntegerField()
    user_review=models.TextField(blank=True)
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField()
    
class billing_address(models.Model):
    user_id=models.ForeignKey(User,default='', on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50,null=True)
    email=models.EmailField()
    phone=models.IntegerField()
    address_1=models.CharField(max_length=200)
    address_2=models.CharField(max_length=200,null=True)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.IntegerField()
    
    
class shipping_address(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50,null=True)
    email=models.EmailField()
    phone=models.IntegerField()
    address_1=models.CharField(max_length=200)
    address_2=models.CharField(max_length=200,null=True)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.IntegerField()
        
        
class shop_cart(models.Model):
    user_id=models.ForeignKey(User,default='', on_delete=models.CASCADE)
    product_id=models.ForeignKey(shop,default='', on_delete=models.CASCADE)
    product_size=models.CharField(max_length=5)
    product_colour=models.CharField(max_length=100)
    product_quantity=models.IntegerField(default=1)
    
    
            
class user_like(models.Model):
    user_id=models.ForeignKey(User,default='', on_delete=models.CASCADE)
    product_id=models.ForeignKey(shop,default='', on_delete=models.CASCADE)
    
