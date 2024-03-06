from django.db import models

from users.models import User
from grocery_store.models import Product


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель')

    def __str__(self):
        return f'Корзина {self.customer.email}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина', related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
