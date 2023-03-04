from django import forms
from django.forms import ModelForm
from .models import *


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        # the widgets are used to styel the form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'gander': forms.Select(attrs={'class': 'form-control', 'placeholder': 'gander'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phonenum': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'manager': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Manager'}),
        }
        # I added the labels dectionary to remove the labels form the form
        labels = {
            'name': '',
            'gander': '',
            'email': '',
            'phonenum': '',
            'address': '',
            'manager': '',
        }
