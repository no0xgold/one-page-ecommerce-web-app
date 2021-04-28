from django import forms
from django.forms import models
from .models import Order

class OrderForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        product = kwargs.pop("product") or None
        super().__init__(*args,**kwargs)
        self.product = product
    class Meta:
        model = Order
        fields = [
            'shipping_address',
            'building_address',
            'amount_of_order',
        ]
    def clean(self, *args,**kwargs):
        cleaned_data= super().clean(*args,**kwargs)
        if self.product != None:
            if not self.product.has_inventory():
                raise forms.ValidationError("this product is out of inventory.")
        return cleaned_data


class ImageForm(forms.ModelForm):
    name =forms.CharField()
    image_field=forms.ImageField()