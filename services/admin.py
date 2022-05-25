from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from xlrd import Book

from .models import Service
from .models import Category


class ServiceResource(resources.ModelResource):

    class Meta:
        model = Service

class ServiceAdmin(ImportExportModelAdmin):
    resource_class = ServiceResource


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category)

