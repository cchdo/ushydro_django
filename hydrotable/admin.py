from django.contrib import admin
from hydrotable.models import Cruise, Program, Parameter, PI, Institution

class ProgramInline(admin.TabularInline):
    model = Program
    extra = 0

class CruiseAdmin(admin.ModelAdmin):
    inlines = [ProgramInline]

admin.site.register(Cruise, CruiseAdmin)
admin.site.register(Parameter)
admin.site.register(PI)
admin.site.register(Institution)
