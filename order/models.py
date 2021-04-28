from django.contrib.auth.signals import user_logged_in
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from django.db.models.expressions import F
from product.models import Product
from django.db.models.signals import pre_save, post_save
from decimal import Decimal
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
    discount = models.IntegerField(default=0,blank=True, null=True)
    inventory_updated = models.BooleanField(default=False)
    amount_of_order= models.IntegerField(default=1,blank=False, null=False)

    def mark_paid(self,custom_amount=None ,save=False):
        paid_amount = self.total
        if custom_amount != None:
            paid_amount = custom_amount
        self.paid = paid_amount
        self.status = "paid"
        
        if not self.inventory_updated and self.product:
            self.product.remove_items_from_inv(count=1, save=True)
            self.inventory_updated = True
        if save == True:
            self.save()
        return self.paid

    def calculate(self, save=False):
        if not self.product:
            return {}
        subtotal = self.product.price
        discount = self.discount
        amount_of_order = self.amount_of_order
        if discount != 0 and discount < 100:
            discount = Decimal(discount / 100)
            save_amount = Decimal(subtotal * discount)
            subtotal = Decimal(subtotal - save_amount)
        if amount_of_order > 1:
            amount_of_order=Decimal(amount_of_order)
            subtotal=Decimal(subtotal * amount_of_order)
        tax_rate=Decimal(0.12)
        tax_total = subtotal * tax_rate
        tax_total = Decimal("%.2f"%(tax_total))
        total = subtotal + tax_total
        total = Decimal("%.2f"%(total))
        totals = {
            "subtotal": subtotal,
            'tax':tax_total,
            'total':total,
        }
        
        for k,v in totals.items():
            setattr(self,k,v)
            if save ==True:
                self.save()
        return totals
def order_pre_save(sender , instance , *args, **kwargs):
    instance.calculate(save=False)

pre_save.connect(order_pre_save, sender=Order)

