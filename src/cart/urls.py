from cart.apps import CartConfig
from django.urls import path

from cart.views import (CartListAPI,
                        AddItemToCartCreateAPIView,
                        ChangeQuantityUpdateAPIView,
                        CartItemDestroyAPIView,
                        CleanCartDestroyAPIView)

app_name = CartConfig.name

urlpatterns = [
    path('', CartListAPI.as_view(), name='cart_list'),
    path('add_to_cart/',
         AddItemToCartCreateAPIView.as_view(),
         name='add_to_cart'),
    path('change_quantity/<int:pk>/',
         ChangeQuantityUpdateAPIView.as_view(),
         name='change_quantity'),
    path('destroy/<int:pk>/',
         CartItemDestroyAPIView.as_view(),
         name='destroy_cart_item'),
    path('clean_cart/', CleanCartDestroyAPIView.as_view(), name='clean_cart'),
]
