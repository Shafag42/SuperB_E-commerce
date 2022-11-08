from django import forms
from .models import  reviews
from django.utils.translation import gettext as _

from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Fieldset, Layout

class ReviewForm(forms.ModelForm):
    class Meta:
        model = reviews
        fields =['price_rating','value_rating','quality_rating', 'nickname', 'summary', 'review']