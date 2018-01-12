from django.contrib import admin

# Register your models here.

from .models import ExternalNumber, InternalNumber, Client


class InternalNumberAdmin(admin.StackedInline):
    model = InternalNumber
    extra = 1

class CustomerClient(admin.StackedInline):
    model = ExternalNumber
    extra = 1

class ExternalNumberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['calling_line',
                           'type_of_access',
                           ]}),
    ]

    inlines = [InternalNumberAdmin]


admin.site.register(ExternalNumber, ExternalNumberAdmin)
