from django import forms
#from django.contrib.auth.models import User
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['name', 'email', 'comment_field']

        widgets={
            "name": forms.TextInput(
                attrs={
                    'class':"form.controls"
                }
            )
        }

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_field']