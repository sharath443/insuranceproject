
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import student_frm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}


class formclass(forms.ModelForm):
    class Meta:
        model = student_frm
        exclude = ['polacy_no']
        widgets = {
            'name': forms.TextInput(attrs={'class':"inputfrms",
                                           'placeholder': 'Enter Your Name'}),
            'date_brth':forms.SelectDateWidget()
        }