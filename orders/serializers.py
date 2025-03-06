from rest_framework import serializers
from products.models import Product
from .models import Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    items = OrderItemSerializer(source='orderItems', many=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_email', 'customer_phone',
                  'items', 'total_price', 'status', 'shipping_address', 'created_at']

    def get_total_price(self, obj):
        return sum(item.quantity * item.product.price for item in obj.orderItems.all())

