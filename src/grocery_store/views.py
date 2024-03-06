from rest_framework.generics import ListAPIView

from grocery_store.models import Category, Subcategory, Product
from grocery_store.serializers import (CategorySerializer,
                                       SubcategorySerializer,
                                       ProductSerializer)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryListAPIView(ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
