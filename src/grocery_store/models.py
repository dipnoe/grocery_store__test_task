from django.db import models
from pytils.translit import slugify

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Наименование', unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category/',
                              verbose_name='Изображение', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-name', ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Subcategory(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Наименование', unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='subcategory/',
                              verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 verbose_name='Категория',
                                 related_name='subcategory')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['-name', ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Наименование', unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    subcategory = models.ForeignKey(Subcategory,
                                    on_delete=models.PROTECT,
                                    verbose_name='Подкатегория')
    price = models.DecimalField(max_digits=6,
                                decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-name', ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product/')
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL,
                                related_name='image', **NULLABLE)
