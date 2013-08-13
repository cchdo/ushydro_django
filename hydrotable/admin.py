from django.contrib import admin
from hydrotable.models import Cruise, Program, Parameter, PI, Institution, Ship
from ordered_model.admin import OrderedModelAdmin

class ProgramInline(admin.TabularInline):
    model = Program
    extra = 0

class CruiseAdmin(admin.ModelAdmin):
    inlines = [ProgramInline]

class ParameterAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')

admin.site.register(Cruise, CruiseAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(PI)
admin.site.register(Institution)
admin.site.register(Ship)
