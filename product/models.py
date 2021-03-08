from django.db import models
from django.db.models.base import Model

class product(models.Model):
    dicription = models.TextField(null= False, max_length=250)
    image = models.ImageField(null=True, blank=True , default="")
    price = models.DecimalField(default=0 ,max_digits=7, decimal_places=2)

