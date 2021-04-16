from django import forms
from django.db import models
from django.forms import fields
from .models import Product
#forms are mostly like models because each form can have a field


class productsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'dicription',
            ]
    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data) < 4:
            raise forms.ValidationError("must be more than 4 letters")
        return data