from django.contrib import admin
from gale.models import Matches, Deliveries
# Register your models here.

from import_export.admin import ImportExportModelAdmin


@admin.register(Matches)
class MatchesAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Matches._meta.get_fields()]


@admin.register(Deliveries)
class DeliveriesAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Deliveries._meta.get_fields()]
