from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField('Пароль устройства', max_length=255)
    wan = models.GenericIPAddressField(protocol='IPv4', unique=True)
    lan = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)

    def __str__(self):
        return self.name


class ExternalNumber(models.Model):
    TYPE_OF_ACCESS = (
        ('any', 'общий'),
        ('specific', 'выделенный'),
        ('free', 'свободный')
    )
    AON = models.CharField(max_length=11, unique=True)
    type_of_access = models.CharField(max_length=10,
                                      choices=TYPE_OF_ACCESS)

    def __str__(self):
        return self.calling_line


class InternalNumber(models.Model):
    TYPE_OF_ACCESS = (
        ('SKD', 'СКД'),
        ('MTT', 'МТТ'),
        ('MOA', 'МОА'),
    )
    type = models.CharField(max_length=20,
                            choices=TYPE_OF_ACCESS,
                            default='no')
    number = models.CharField(max_length=6)
    password = models.CharField(max_length=20)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.inner_number


class Customer(models.Model):
    STATUS = (
        ('1', 'enabled'),
        ('0', 'disabled'),
    )

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='0')
    address = models.CharField(max_length=255)
    InternalNumber = models.ForeignKey(InternalNumber,
                                       on_delete=models.SET_NULL,
                                       blank=True,
                                       null=True)
    ExternalNumber = models.ForeignKey(ExternalNumber,
                                       on_delete=models.SET_NULL,
                                       blank=True,
                                       null=True)
    date_last_change = models.DateField(auto_now=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.customer
