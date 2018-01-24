from django import forms
from apps.phone.models import Customer, Device, Number


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'status', 'address', 'description', )

