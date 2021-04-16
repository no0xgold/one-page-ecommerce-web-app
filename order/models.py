from django.contrib.auth.signals import user_logged_in
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from product.models import Product

# Create your models here.
 
User = get_user_model()

ORDER_STATUS_CHOICE = (
    ('created','Created'),
    ('stale', 'Stale'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

class Order(models.Model):
    user = models.ForeignKey(User , null=True, on_delete=models.SET_NULL)#if admin delete from my system, the order record wouldn't be deleted
    product = models.ForeignKey(Product ,null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICE, default='created')
    subtotal = models.DecimalField(default=0.00 ,max_digits=7, decimal_places=2)
    tax = models.DecimalField(default=0.00 ,max_digits=7, decimal_places=2)
    total = models.DecimalField(default=0.00 ,max_digits=7, decimal_places=2)
    paid = models.DecimalField(default=0.00 ,max_digits=7, decimal_places=2)
    shipping_address = models.TextField(blank=True, null=True)
    building_address = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)