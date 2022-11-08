from urllib import request
from django import forms
from django.contrib.auth.forms import (UserCreationForm, 
AuthenticationForm, PasswordResetForm ,SetPasswordForm,PasswordChangeForm,UsernameField)
from django.contrib.auth import get_user_model
from .models import Account_Information,ShippingAddress,Forgot_password,User

class UserRegisterForm(UserCreationForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'input-text', 'placeholder': 'Your Password'}))

    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'input-text', 'placeholder': 'Your Confirm Password'}))
                                                            
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-text',
                                                'placeholder': "Your First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'input-text',
                                                'placeholder': "Your Last Name"}),
            'email': forms.EmailInput(attrs={'class': 'input-text',
                                            'placeholder': "Your Email Address"}),
            'username': forms.TextInput(attrs={'class': 'input-text',
                                                'placeholder': "Your Username"})
        }

class LoginForm(AuthenticationForm):  # type: ignore

    username: UsernameField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Your Username"}))  # type: ignore
    password: forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                'placeholder': "Your Password"}))  # type: ignore
        


    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Password and confirm password doesn't match")
        return password2


class LoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control ",
        "placeholder": "Username"
    }))

    password =forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control ",
        "placeholder": "Password"
    }))

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label="Email Address", 
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }))


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(required=True, label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your New Password'
            }))
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Your New Password'
            }))

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, label='Old Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Old Password'
            }))
    new_password1 = forms.CharField(required=True, label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your New Password'
            }))
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Your New Password'
            }))


class Account_InformationForm(forms.ModelForm):
    class Meta:
        model = Account_Information
        fields='__all__'
        
        widgets={
            "first_name": forms.TextInput(
                attrs={
                    'class':"form-control",
                    'placeholder':"First name"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    'class':"form-control",
                    'placeholder': "Last name"
                }
            )
        }


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields= '__all__'


class Forgot_passwordForm(forms.ModelForm):
    class Meta:
        model = Forgot_password
        fields='__all__'
        
        widgets={
            "email": forms.EmailInput(
                attrs={
                    'class':"form-control",
                    'placeholder':"Email"
                }
            ),
        }

