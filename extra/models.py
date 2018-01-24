from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.


class Customer(models.Model):
    STATUS = (
        ('1', 'Enabled'),
        ('0', 'Disabled'),
    )

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='0')
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    date_last_change = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField('Пароль устройства', max_length=255)
    wan = models.GenericIPAddressField(protocol='IPv4', unique=True)
    lan = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)

    def __str__(self):
        return self.name


class InternalNumber(models.Model):
    TYPE_OF_ACCESS = (
        ('SKD', 'СКД'),
        ('MTT', 'МТТ'),
        ('MOA', 'МОА'),
    )
    type = models.CharField(max_length=20,
                            choices=TYPE_OF_ACCESS,
                            default='MTT')
    number = models.CharField(max_length=6, unique=True)
    password = models.CharField(max_length=20)

    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)

    device = models.ForeignKey(Device,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)

    def __str__(self):
        return self.number


class ExternalNumber(models.Model):
    TYPE_OF_ACCESS = (
        ('any', 'общий'),
        ('specific', 'выделенный'),
        ('free', 'свободный')
    )
    AON = models.CharField(max_length=11)
    type_of_access = models.CharField(max_length=10,
                                      choices=TYPE_OF_ACCESS)
    '''
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    '''
    internalnumber = models.ForeignKey(InternalNumber,
                                       on_delete=models.CASCADE,
                                       blank=True,
                                       null=True)

    def __str__(self):
        return self.AON


