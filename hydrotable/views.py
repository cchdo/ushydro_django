from django.http import HttpResponse
from django.shortcuts import render

from hydrotable.models import Cruise, Parameter

def index(request):
    load_cruises = Cruise.objects.all()
    cruises = {}
    for cruise in load_cruises:
        cruises[cruise] = cruise.program_set.all()

    parameters = Parameter.objects.all()
    context = {'cruises': cruises,
                'parameters': parameters
                }
    return render(request, 'hydrotable/index.html', context)

