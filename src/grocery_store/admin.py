from django.contrib import admin

from grocery_store.models import Category, Subcategory, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', ]
    readonly_fields = ['slug', ]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'category', ]
    readonly_fields = ['slug', ]


class ImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['name', 'slug', 'subcategory', 'price', ]
    readonly_fields = ['slug', ]
