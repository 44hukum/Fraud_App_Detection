from attr import fields
from django.contrib.auth.models import User
from django import forms

from usermanagement.models import CustomUser

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username','first_name','email','phonenumber')
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password']:
            raise forms.ValidationError('Password dont match')
        return cd['password2']