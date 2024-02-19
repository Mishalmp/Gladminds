from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryView,ProductView,SubcategoryView,ListSubcategoryView,ListProductView

router=DefaultRouter()
router.register('category',CategoryView)
router.register('subcategory',SubcategoryView)
router.register('product',ProductView)

urlpatterns = [
   path('',include(router.urls)),
   path('listproducts/',ListProductView.as_view()),
   path('listsubcategories/',ListSubcategoryView.as_view()),

   
]
