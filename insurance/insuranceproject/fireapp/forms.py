from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import fire_mdl


class fire_frm(forms.ModelForm):
    class Meta:
        model = fire_mdl
        exclude = ['polacy_no']
        widgets = {
            'name': forms.TextInput(attrs={'class':"inputfrms",
                                           'placeholder': 'Enter Your type of property'}),
        }