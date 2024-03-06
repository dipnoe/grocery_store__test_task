from rest_framework import serializers

from grocery_store.models import (Category,
                                  Subcategory,
                                  Product)


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category', 'slug', 'image', ]


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'subcategory', ]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(
        source='subcategory.category'
    )
    subcategory = serializers.StringRelatedField()
    images = serializers.StringRelatedField(source='image', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'slug', 'subcategory', 'category', 'price', 'images']
