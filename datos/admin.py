from django.contrib import admin

# Register your models here.
from datos.models import Datos


class DatosAdmin(admin.ModelAdmin):

    list_display = (
        'fecha',
        'concepto',
        'ingreso',
        'gasto',
        'total'
    )
    search_fields = ('gasto',)
    list_filter = ('ingreso', 'gasto', 'fecha')

admin.site.register(Datos, DatosAdmin)