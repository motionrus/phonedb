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


class Number(models.Model):
    TYPE_OF_INTNUM = (
        ('SKD', 'СКД'),
        ('MTT', 'МТТ'),
        ('MOA', 'МОА'),
    )
    TYPE_OF_EXT = (
        ('any', 'общий'),
        ('specific', 'выделенный'),
        ('free', 'свободный')
    )
    internal_type = models.CharField(max_length=20,
                            choices=TYPE_OF_INTNUM,
                            default='MTT')
    internal_number = models.CharField(max_length=6, unique=True)
    internal_password = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    device = models.ForeignKey(Device,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    AON = models.CharField(max_length=11)
    type_of_access = models.CharField(max_length=10,
                                      choices=TYPE_OF_EXT)

    def __str__(self):
        return 'int: "{}", ext: "{}"'.format(self.internal_number, self.AON)
