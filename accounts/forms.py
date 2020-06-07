from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}), required=False)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}), required=False)
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name or first_name is '':
            raise ValidationError('*')
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name or last_name is '':
            raise ValidationError('*')
        return last_name
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken, please try another one.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email Already taken")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        validate_password(password2)
        return password2
class ModalLoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}), required=False)
