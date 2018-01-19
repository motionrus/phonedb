from django.contrib import admin

# Register your models here.

from .models import ExternalNumber, InternalNumber, Customer

admin.site.register(ExternalNumber)
admin.site.register(InternalNumber)
admin.site.register(Customer)