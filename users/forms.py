from django import forms
from django.contrib.auth import get_user_model
from django.http import request
from django.forms import fields
User = get_user_model()

not_allowed_username=['amir']
class RegisterForm(forms.Form):
    username = forms.CharField()
    email= forms.EmailField()
    password1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'user-password'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'user-confirm-password'
            }
        )
    )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        #for iexact doesn't matter if this is capital or not
        #username=UserName
        if username in not_allowed_username:
            raise forms.ValidationError('this  is invalid username, choose another.')
        if qs.exists():
            raise forms.ValidationError('this  is invalid username, choose another.')
        return username

    def clean_email(self):
        email= self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        #for iexact doesn't matter if this is capital or not
        #username=UserName
        if qs.exists():
            raise forms.ValidationError('this  is invalid email, this email is already in use.')
        return email

#by default these two are required
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            "id":"user-password"}
    ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'user-password'
            }
        )
    )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        #for iexact doesn't matter if this is capital or not
        #username=UserName
        if not qs.exists():
            raise forms.ValidationError('this  is invalid user')
        if qs.count() != 1:
            raise forms.ValidationError("this is an invalid user.")
        return username



    
