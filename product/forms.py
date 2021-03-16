from django import forms

#forms are mostly like models because each form can have a field
class productsForm(forms.Form):
    title = forms.CharField()