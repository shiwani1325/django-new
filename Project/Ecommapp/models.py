from django.db import models
from base.models import BaseModel
# Create your models here.



class Category(BaseModel):
    category_name=models.CharField(max_length=150)
    slug=models.SlugField(unique=True, null=True, blank=True)
    category_image=models.ImageField(upload_to="categories")
    


    
class Product(BaseModel):
    product_name=models.CharField(max_length=150)
    slug=models.SlugField(unique=True,  null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product")
    price=models.IntegerField()
    product_description=models.CharField(max_length=200)


class ProductImage(BaseModel):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image=models.ImageField(upload_to="product")










