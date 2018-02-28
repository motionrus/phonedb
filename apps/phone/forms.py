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


class TestDeviceForm(forms.Form):
    name = forms.CharField(max_length=255)
    login = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    wan = forms.GenericIPAddressField(protocol='IPv4')
    lan = forms.GenericIPAddressField(protocol='IPv4', required=False)


class EnhancedNumberForm(NumberForm):
    STATUS = (
        ('1', 'Активный'),
        ('0', 'Отключен'),
    )

    name = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices=STATUS)
    address = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    device_name = forms.CharField(max_length=255)
    device_login = forms.CharField(max_length=255)
    device_password = forms.CharField(max_length=255)
    device_wan = forms.GenericIPAddressField(protocol='IPv4')
    device_lan = forms.GenericIPAddressField(protocol='IPv4', required=False)
    ArticleFormSet = forms.formset_factory(CustomerForm)

    def clean(self):
        cleaned_data = super(EnhancedNumberForm, self).clean()

        Current_device = Device()
        Current_customer = Customer()
        name = cleaned_data.get("name")
        status = cleaned_data.get("status")
        address = cleaned_data.get("address")
        description = cleaned_data.get("description")

        Current_customer.name = name
        Current_customer.status = status
        Current_customer.address = address
        Current_customer.description = description

        device_name = cleaned_data.get("device_name")
        device_login = cleaned_data.get("device_login")
        device_password = cleaned_data.get("device_password")
        device_wan = cleaned_data.get("device_wan")
        device_lan = cleaned_data.get("device_lan")

        Current_device.name = device_name
        Current_device.login = device_login
        Current_device.password = device_password
        Current_device.wan = device_wan
        Current_device.lan = device_lan

        self.instance.device = Current_device
        self.instance.customer = Current_customer
        if self.is_valid():
            self.instance.device.save()
            self.instance.customer.save()

