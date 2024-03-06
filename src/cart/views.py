from django.http import JsonResponse
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from cart.models import Cart, CartItem
from cart.serializers import (CartSerializer,
                              CartItemSerializer,
                              AddAndChangeItemSerializer)

from users.permissions import IsCartItemOwner, IsCartOwner


class CartListAPI(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Cart.objects.filter(customer=self.request.user)
        return queryset


class AddItemToCartCreateAPIView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = AddAndChangeItemSerializer
    permission_classes = [IsAuthenticated, IsCartOwner]


class ChangeQuantityUpdateAPIView(UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = AddAndChangeItemSerializer
    permission_classes = [IsAuthenticated, IsCartItemOwner]


class CartItemDestroyAPIView(DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = AddAndChangeItemSerializer
    permission_classes = [IsAuthenticated, IsCartItemOwner]


class CleanCartDestroyAPIView(DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = AddAndChangeItemSerializer
    permission_classes = [IsAuthenticated, IsCartItemOwner]

    def delete(self, request, *args, **kwargs):
        customer = request.user
        cart = Cart.objects.get(customer=customer)
        cart_items = CartItem.objects.filter(cart=cart)
        [i.delete() for i in cart_items]
        return JsonResponse({
            'success': True
        })
