from django.db import models
from products.models import Product

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(unique=True)
    customer_phone = models.CharField(max_length=13)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.CharField(max_length=255, default='Nowhere')

    def __str__(self):
        return self.customer_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderItems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orderItems')
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
