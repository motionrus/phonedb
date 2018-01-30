from django import forms
from apps.phone.models import Customer, Device, Number


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'status', 'address', 'description', )


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ('internal_type',
                  'internal_number',
                  'internal_password',
                  'device',
                  'AON')


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = (
            'name',
            'login',
            'password',
            'wan',
        )


class CreateNumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = (
            'internal_number',
            'internal_type',
            'internal_password',
            'device',
            'AON',
        )