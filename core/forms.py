from django import forms
from django.db.models import fields

from core.models import ContactUs,ContactInfo, Subscriber

from django.forms import widgets

class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = ['first_name','email','company','telephone','address_one','address_two','comment' ]
        widgets = {
        'first_name'  : forms.TextInput(attrs={
                                        'type' :"text", 
                                        'title' : "First Name",
                                        'class' : "input-text"}),
        'email'     :   forms.TextInput(attrs={
                                        
                                        'class' : "input-text"}),
        'company'   :   forms.TextInput(attrs={
                                        'type' :"text",
                                        'title' : "Company",
                                        'class' : "input-text"}),
        'telephone' :   forms.TextInput(attrs={
                                        'type' :"text",
                                       
                                        'class' : "input-text  required-entry",}),
        'address_one' : forms.TextInput(attrs={
                                        'type' :"text",
                                        'title' : "Street Address",
                                        'class' : "input-text"}),
        'address_two' : forms.TextInput(attrs={
                                        'type' :"text",
                                        'title' : "Street Address 2",
                                        'class' : "input-text"}),
        'comment'   : forms.Textarea(attrs={
                                        'title' : "Comment",
                                        'class' : "input-text ",
                                        'cols' : "5",
                                        'rows' : "3"}),
        }

    def clean(self):
        data = self.cleaned_data.get('first_name')
        if len(data) < 2:
            raise forms.ValidationError("Name must be at least 2 chars. long.")
        return self.cleaned_data

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = "__all__"
    
        widgets = {
            'first_name': forms.TextInput(attrs={
                                        'type' :"text", 
                                        'title' : "First Name",
                                        'class' : "input-text required-entry"}),
            'last_name': forms.TextInput(attrs={
                                        'type' :"text",
                                        'title' : "Last Name",
                                        'class' : "input-text required-entry"}),
            'company': forms.TextInput(attrs={
                                        'type' :"text",
                                        'title' : "",
                                        'class' : "input-text required-entry"}),
            'telephone': forms.TextInput(attrs={
                                        'type' :"text",
                                        'title' : "",
                                        'class' : "input-text required-entry"}),
            'fax': forms.TextInput(attrs={
                                        'type' :"text",
                                        'title' : "",
                                        'class' : "input-text required-entry"}),
            'address_one': forms.TextInput(attrs={
                                        'type' :"text",
                                        'title' : "",
                                        'class' : "input-text required-entry"}),
            'address_two': forms.TextInput(attrs={
                                        'type' :"text",
                                        'title' : "",
                                        'class' : "input-text required-entry"}),
            'zip': forms.TextInput(attrs={
                                        'type' :"text", 
                                        'title' : "",
                                        'class' : "input-text required-entry"}),
                                        }



class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'
        widgets = {
            'email' : widgets.EmailInput(attrs={'class': 'input-text required-entry validate-email', 'placeholder': 'Enter your email address'} ),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use")
        return 