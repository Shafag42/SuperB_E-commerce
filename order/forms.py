from django import forms
from django.forms import fields, widgets

from order.models import CheckoutBilling

class CheckoutBillingForm(forms.ModelForm):
    class Meta:
        model = CheckoutBilling
        fields = ['first_name', 'last_name', 'company', 'email', 'address', 'country','telephone', 'fax',]
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'input-text'}),
            'last_name': widgets.TextInput(attrs={'class': 'input-text'}),
            'company': widgets.TextInput(attrs={'class': 'input-text'}),
            'email': widgets.TextInput(attrs={'class': 'input-text'}),
            'address': widgets.TextInput(attrs={'class': 'input-text'}),
            'telephone': widgets.TextInput(attrs={'class': 'input-text'}),
            'fax': widgets.TextInput(attrs={'class': 'input-text'}),
        }