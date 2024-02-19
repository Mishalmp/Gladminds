from django.db import models

# Create your models here.


class Categories(models.Model):
    category_name=models.CharField(max_length=100)
    category_image=models.ImageField(upload_to="categories/",null=True)
    is_block=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category_name}"

class Subcategories(models.Model):
    sub_category_name=models.CharField(max_length=100)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    sub_category_image=models.ImageField(upload_to="sub_categories/",null=True)
    is_block=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sub_category_name}"


class Products(models.Model):
    item=models.CharField(max_length=100)
    subcategory=models.ForeignKey(Subcategories,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField(default=0)
    is_block=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item}"



class ProductImages(models.Model):
    image=models.ImageField(upload_to="products/",null=True)
    product=models.ForeignKey(Products,related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.item} image"







