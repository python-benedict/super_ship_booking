from dataclasses import field
from django import forms
from .models import PassengerBaseModel

class PassengerForm(forms.ModelForm):

    class Meta:
        model = PassengerBaseModel
        fields = '__all__'