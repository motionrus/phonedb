# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-12 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_to_MG', models.CharField(choices=[('no', 'нет'), ('DTMF', 'донабор'), ('direct number', 'прямой номер')], default='no', max_length=10)),
                ('active', models.CharField(choices=[('1', 'enabled'), ('0', 'disabled')], default='0', max_length=10)),
                ('customer', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('date_last_change', models.DateField(auto_now=True)),
                ('description', models.DateField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExternalNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calling_line', models.CharField(max_length=11, unique=True)),
                ('type_of_access', models.CharField(choices=[('any', 'общий'), ('specific', 'выделенный')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inner_number', models.CharField(max_length=10)),
                ('inner_number_passwd', models.CharField(max_length=20)),
                ('device', models.CharField(max_length=20)),
                ('login_device', models.CharField(max_length=20)),
                ('pass_device', models.CharField(max_length=20)),
                ('wan', models.GenericIPAddressField(protocol='IPv4')),
                ('lan', models.GenericIPAddressField(protocol='IPv4')),
                ('calling_line_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.ExternalNumber')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.Number'),
        ),
    ]