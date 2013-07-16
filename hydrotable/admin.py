from django.contrib import admin
from hydrotable.models import Cruise, Cell, Parameter

class CellInline(admin.StackedInline):
    model = Cell
    extra = 0

class CruiseAdmin(admin.ModelAdmin):
    inlines = [CellInline]

admin.site.register(Cruise, CruiseAdmin)
admin.site.register(Parameter)
