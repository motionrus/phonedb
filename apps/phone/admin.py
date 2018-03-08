from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

from .models import Number, Customer, Device

admin.site.register(Number)
#admin.site.register(Customer)
admin.site.register(Device)


class NumbersAdmin(admin.TabularInline):
    model = Number
    extra = 1
    exclude = ('type_of_access',)
    readonly_fields = ('type_of_access',)


class CustomerAdmin(admin.ModelAdmin):
    inlines = [NumbersAdmin]



admin.site.register(Customer,  CustomerAdmin)