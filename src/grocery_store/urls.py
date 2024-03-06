from django.urls import path

from grocery_store.apps import GroceryStoreConfig
from grocery_store.views import (CategoryListAPIView,
                                 SubcategoryListAPIView,
                                 ProductListAPIView)

app_name = GroceryStoreConfig.name

urlpatterns = [
    path('category/list/', CategoryListAPIView.as_view(),
         name='category_list'),
    path('subcategory/list/', SubcategoryListAPIView.as_view(),
         name='subcategory_list'),
    path('product/list/', ProductListAPIView.as_view(),
         name='product_list'),
]
