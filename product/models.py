from django.db import models
from django.db.models.base import Model

class product(models.Model):
    title = models.CharField(max_length=220, default="")
    dicription = models.TextField(null= True, max_length=250, blank=True)
    image = models.ImageField(null=True, blank=True , default="")
    price = models.DecimalField(default=0 ,max_digits=7, decimal_places=2)

