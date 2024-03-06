from rest_framework import serializers

from cart.models import Cart, CartItem
from grocery_store.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(read_only=True)
    product = serializers.StringRelatedField()
    price = serializers.StringRelatedField(source='product.price')

    class Meta:
        model = CartItem
        fields = ['product_id', 'product', 'price', 'quantity', ]


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    items_count = serializers.SerializerMethodField()
    total_sum = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['customer', 'cart_items', 'items_count', 'total_sum', ]

    def get_items_count(self, instance):
        cart_items = CartItem.objects.filter(cart=instance)
        total_quantity = sum([i.quantity for i in cart_items])
        return total_quantity

    def get_total_sum(self, instance):
        cart_items = CartItem.objects.filter(cart=instance)
        total_sum = sum([i.product.price * i.quantity for i in cart_items])
        return total_sum


class AddAndChangeItemSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )
    quantity = serializers.IntegerField(default=1, min_value=1)

    def create(self, validated_data):
        customer = self.context['request'].user
        cart, created = Cart.objects.get_or_create(customer=customer)
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')

        try:
            CartItem.objects.get(cart=cart, product=product)
            raise serializers.ValidationError("Продукт уже есть в корзине.")
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                cart=cart,
                product=product,
                quantity=quantity
            )
        return cart_item

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
