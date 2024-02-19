from rest_framework import serializers
from .models import Categories,Subcategories,Products,ProductImages




class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Categories
        fields="__all__"

class SubcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subcategories
        fields="__all__"


class ListSubcategoriesSerializer(serializers.ModelSerializer):
    category=CategorySerializer(read_only=True)
    class Meta:
        model=Subcategories
        fields="__all__"


class ProductImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductImages
        fields="__all__"


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields="__all__"

class ListProductsSerializers(serializers.ModelSerializer):
    images=ProductImagesSerializers(many=True)
    subcategory=ListSubcategoriesSerializer(read_only=True)
    class Meta:
        model=Products
        fields="__all__"



