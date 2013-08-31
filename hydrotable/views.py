from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from hydrotable.models import Cruise, Parameter, Program

#@cache_page(60 * 15)
def index(request):
    cruises = Cruise.objects.all().prefetch_related('program_set',
    'chief_scientist', 'ship',)

    parameters = Parameter.objects.all()
    programs = Program.objects.all().prefetch_related('pi')

    pi_names = {}
    for program in programs:
        pi_names[program.id] = program.pi.name

    context = {'cruises': cruises,
                'parameters': parameters,
                'pi_names': pi_names,
                }
    return render(request, 'hydrotable/index.html', context)

