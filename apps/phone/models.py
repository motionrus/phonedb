from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class ExternalNumber(models.Model):
    TYPE_OF_ACCESS = (
        ('any', 'общий'),
        ('specific', 'выделенный'),
    )
    calling_line = models.CharField(max_length=11, unique=True)
    type_of_access = models.CharField(max_length=10,
                                      choices=TYPE_OF_ACCESS)

    def __str__(self):
        return self.calling_line


class InternalNumber(models.Model):
    TYPE_OF_ACCESS = (
        ('no', 'нет'),
        ('DTMF', 'донабор'),
        ('direct number', 'прямой номер'),
    )
    access_to_MG = models.CharField(max_length=20,
                                    choices=TYPE_OF_ACCESS,
                                    default='no')
    calling_line_id = models.ForeignKey(ExternalNumber,
                                        on_delete=models.SET_NULL,
                                        blank=True,
                                        null=True)
    inner_number = models.CharField(max_length=10)
    inner_number_passwd = models.CharField(max_length=20 )
    device = models.CharField(max_length=20)
    login_device = models.CharField(max_length=20)
    pass_device = models.CharField('Пароль устройства', max_length=20)
    wan = models.GenericIPAddressField(protocol='IPv4')
    lan = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)

    def __str__(self):
        return self.inner_number

class Client(models.Model):
    STATUS = (
        ('1', 'enabled'),
        ('0', 'disabled'),
    )
    phone_number = models.ForeignKey(InternalNumber,
                                     on_delete=models.CASCADE)
    active = models.CharField(max_length=10,
                              choices=STATUS,
                              default='0')
    customer = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date_last_change = models.DateField(auto_now=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.customer
