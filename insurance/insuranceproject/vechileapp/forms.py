from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import vmodel


class vehicle_frm(forms.ModelForm):
    class Meta:
        model = vmodel
        exclude = ['polacy_no']