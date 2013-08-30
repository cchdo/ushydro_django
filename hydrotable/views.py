from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from hydrotable.models import Cruise, Parameter

#@cache_page(60 * 15)
def index(request):
    cruises = Cruise.objects.all().prefetch_related('program_set',
    'chief_scientist', 'ship',)

    parameters = Parameter.objects.all()
    context = {'cruises': cruises,
                'parameters': parameters
                }
    return render(request, 'hydrotable/index.html', context)

