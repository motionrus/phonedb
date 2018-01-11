from django.db import models

# Create your models here.

class InnerNumber(models.Model):
    TYPE_OF_ACCESS = (
        ('no', 'нет'),
        ('DTMF', 'донабор'),
        ('direct number', 'прямой номер'),
    )
    STATUS = (
        ('1', 'enabled'),
        ('0', 'disabled'),
    )
    active = models.CharField(max_length=10,
                              choices=STATUS,
                              default='0')
    inner_number = models.CharField(max_length=10)
    inner_number_passwd = models.CharField(max_length=20)
    customer = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    calling_line_id = models.CharField(max_length=11)
    access_to_MG = models.CharField(max_length=10,
                                    choices=TYPE_OF_ACCESS,
                                    default='no')
    device = models.CharField(max_length=20)
    login_device = models.CharField(max_length=20)
    pass_device = models.CharField(max_length=20)
    wan = models.GenericIPAddressField(protocol='IPv4')
    lan = models.GenericIPAddressField(protocol='IPv4')
    data_create = models.DateField(auto_now=True)
    description = models.DateField(max_length=255)


class ExtraNumber(models.Model):
    pass