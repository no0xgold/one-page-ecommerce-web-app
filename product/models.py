from django.db import models
from django.db.models.base import Model
from django.conf import settings 
from .storages import ProtectedStorage
User = settings.AUTH_USER_MODEL


class Product(models.Model):
    user = models.ForeignKey(User, null=True ,on_delete=models.SET_NULL)
    title = models.CharField(max_length=220, default="")
    dicription = models.TextField(null= True, max_length=250, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    media = models.FileField(storage=ProtectedStorage ,upload_to='product/', null=True, blank=True)
    price = models.DecimalField(default=0.00 ,max_digits=7, decimal_places=2)
    inventory = models.IntegerField(default=0 )
    featured = models.BooleanField(default=False)
    def has_inventory(self):
        return self.inventory > 0
        #return  self.inventory > 0 #Give us True or False

    def remove_items_from_inv(self, count=1, save=True):
        current_inv = self.inventory
        current_inv -= count
        self.inventory = current_inv
        if save == True:
            self.save()
        return self.inventory

