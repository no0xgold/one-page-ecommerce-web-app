from django.db import models
from django.db.models.base import Model
from django.conf import settings 

User = settings.AUTH_USER_MODEL
class Product(models.Model):
    user = models.ForeignKey(User, null=True ,on_delete=models.SET_NULL)
    title = models.CharField(max_length=220, default="")
    dicription = models.TextField(null= True, max_length=250, blank=True)
    image = models.ImageField(null=True, blank=True , default="")
    price = models.DecimalField(default=0.00 ,max_digits=7, decimal_places=2)
    inventory = models.IntegerField(default=0 )
    featured = models.BooleanField(default=False)
    def has_inventory(self):
        return  self.inventory > 0 #Give us True or False

