from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from django.core.exceptions import ValidationError

COLLECTIVE_NUMBER = ['84959830402', '84959830535']


class Customer(models.Model):
    STATUS = (
        ('1', 'Активный'),
        ('0', 'Отключен'),
    )

    name = models.CharField(max_length=255, unique=True)
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
        return "{} ({})".format(self.name, self.wan)


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
    internal_password = models.CharField(max_length=20, blank=True, null=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    device = models.ForeignKey(Device,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    AON = models.CharField(max_length=11, blank=True, null=True)
    type_of_access = models.CharField(max_length=10,
                                      choices=TYPE_OF_EXT, default='free')

    def __str__(self):
        return '"{}" <=> "{}"'.format(self.internal_number, self.AON)


@receiver(pre_save, sender=Number)
def my_handler(sender, instance, **kwargs):
    instance.type_of_access = 'specific'
    if instance.AON == '':
        instance.type_of_access = 'free'
        return
    if instance.AON in COLLECTIVE_NUMBER:
        instance.type_of_access = 'any'
        return


@receiver(post_delete, sender=Number)
def remove_client_with_no_numbers(sender, instance, **kwargs):
    customer = instance.customer
    if not Number.objects.filter(customer=customer):
        print('удаление клиента')
        customer.delete()
