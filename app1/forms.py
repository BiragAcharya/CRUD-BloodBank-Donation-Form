from django import forms
from .models import Register

class donateBlood_edit(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['donorname', 'blood_group','unit','age']