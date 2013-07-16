from django.http import HttpResponse
from django.shortcuts import render

from hydrotable.models import Cruise, Parameter

def index(request):
    cruises = Cruise.objects.all()
    parameters = Parameter.objects.all()
    context = {'cruises': cruises,
                'parameters': parameters
                }
    return render(request, 'hydrotable/index.html', context)

