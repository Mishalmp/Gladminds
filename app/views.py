from django.shortcuts import render
from .serializers import CategorySerializer,SubcategoriesSerializer,ListSubcategoriesSerializer,ProductImagesSerializers,ProductsSerializers,ListProductsSerializers
from .models import Categories,Subcategories,Products,ProductImages


from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class CategoryView(ModelViewSet):
    serializer_class=CategorySerializer
    queryset=Categories.objects.all()

class SubcategoryView(ModelViewSet):
    serializer_class=SubcategoriesSerializer
    queryset=Subcategories.objects.all()

class ListSubcategoryView(ListAPIView):
    serializer_class=ListSubcategoriesSerializer
    queryset=Subcategories.objects.all()


class ProductView(ModelViewSet):
    serializer_class=ProductsSerializers
    queryset=Products.objects.all()

class ListProductView(ListAPIView):
    serializer_class=ListProductsSerializers
    queryset=Products.objects.all()



