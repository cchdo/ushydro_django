import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from hydrotable.models import Cruise, Parameter, Program
from collections import namedtuple

#@cache_page(60 * 15)
def index(request):
    cruises = Cruise.objects.all().prefetch_related('program_set',
    'chief_scientist', 'ship',)

    parameters = Parameter.objects.all()
    programs = Program.objects.all().prefetch_related('pi')

    for cruise in cruises:
        cruise.generate_program_dict()
    pi_names = {}
    for program in programs:
        pi_names[program.id] = program.pi.name

    context = {'cruises': cruises,
                'parameters': parameters,
                'pi_names': pi_names,
                'custom': "False",
                }
    return render(request, 'hydrotable/index.html', context)

def make_cell_obj(text, href=None, status=None):
    return {
            "text": text,
            "href": href,
            "status": status
            }

def as_json(request):
    cruises = Cruise.objects.all().prefetch_related('program_set',
    'chief_scientist', 'ship',)

    parameters = Parameter.objects.all()
    programs = Program.objects.all().prefetch_related('pi')

    hard_coded_cols = [
            "Cruise",
            "Dates",
            "Expocode",
            "Ship",
            "Days",
            "Stations",
            "Ports",
            "Chief Scientist",
            ]

    for cruise in cruises:
        cruise.generate_program_dict()
    pi_names = {}
    for program in programs:
        pi_names[program.id] = program.pi.name

    params = []
    param_map = {}
    for param in parameters:
        params.append(param.name)
        param_map[param.name] = param.id

    cols = hard_coded_cols + params

    rows = []

    for cruise in cruises:
        row_obj = {}
        for col in cols:
            ## handle all the special cases..
            if col == "Cruise":
                row_obj[col] = [make_cell_obj(cruise.name_with_year)]
            if col == "Dates":
                row_obj[col] = [make_cell_obj(cruise.safe_start_date + " to " + cruise.safe_end_date)]
            if col == "Ship":
                row_obj[col] = [make_cell_obj(cruise.ship.name,
                    href=cruise.ship.url
                    )]
            if col == "Expocode":
                status = None
                if cruise.expocode_link:
                    status = "isdata"
                row_obj[col] = [make_cell_obj(cruise.safe_expocode,
                        href=cruise.expocode_link,
                        status=status)]
            if col == "Days":
                row_obj[col] = [make_cell_obj(cruise.safe_days)]
            if col == "Stations":
                row_obj[col] = [make_cell_obj(cruise.stations)]
            if col == "Ports":
                row_obj[col] = [make_cell_obj(cruise.safe_start_port + " - " + cruise.safe_end_port)]
            if col == "Chief Scientist":
                cells = [make_cell_obj(cs.name) for cs in
                        cruise.chief_scientist.all()]
                row_obj[col] = cells

            # this is everyone else
            if col in param_map and param_map[col] in cruise.parameters:
                param_id = param_map[col]
                cells = []
                for program in cruise.program_dict[param_id]:
                    cells.append(make_cell_obj(pi_names[program.id],
                        status=program.html_classes, href=program.url))
                row_obj[col] = cells



        rows.append(row_obj)

    response = HttpResponse(json.dumps({"columns":cols, "rows":rows}),
            content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def custom(request):
    parameters = Parameter.objects.all()
    context = {
            'parameters': parameters,
            }

    return render(request, 'hydrotable/custom.html', context)

def step2(request):
    if request.method != "POST":
        return redirect(custom)
    if u"build_table" in request.POST:
        url = "?"
        for item in request.POST.getlist(u'columns'):
            s = item[:1] + "[]=" + item[2:] + "&"
            url += s
        return redirect("/hydrotable/custom/build/" +  url)


        
        
    # Probably the worst code I've ever written
    ParamList = namedtuple('ParamList', ['p_id', 'param_name'])
    desired_list = []
    if request.method == 'POST':
        desired = request.POST.getlist(u"columns")
        id_list = []
        param_list = []
        for param in desired:
            if param[2:] == "dates":
                desired_list.append(ParamList(param, "Dates"))
            if param[2:] == "expocode":
                desired_list.append(ParamList(param, "Expocode"))
            if param[2:] == "ship":
                desired_list.append(ParamList(param, "Ship"))
            if param[2:] == "days":
                desired_list.append(ParamList(param, "Days"))
            if param[2:] == "stations":
                desired_list.append(ParamList(param, "Stations"))
            if param[2:] == "ports":
                desired_list.append(ParamList(param, "Ports"))
            if param[2:] == "cs":
                desired_list.append(ParamList(param, "Chief Scientist"))
            if param[2:].isdigit():
                id_list.append(int(param[2:]))
                param_list.append(param)
        parameters = Parameter.objects.in_bulk(id_list)
        parameters = [parameters[id].name for id in id_list]
        for param, param_name in zip(param_list, parameters):
            desired_list.append(ParamList(param, param_name))

    context = {
            'parameters': desired_list,
            }

    return render(request, 'hydrotable/step2.html', context)

def build(request):
    if request.method != "GET":
        return redirect(custom)
    cruises = Cruise.objects.all().prefetch_related('program_set',
    'chief_scientist', 'ship',)

    for cruise in cruises:
        cruise.generate_program_dict()
    custom_list = request.GET.getlist(u'p[]')
    custom_params = []
    for custom in custom_list:
        if custom.isdigit():
            custom_params.append(int(custom))
    parameters = Parameter.objects.in_bulk(custom_params)
    params = []
    for custom in custom_list:
        if custom.isdigit():
            params.append(parameters[int(custom)])
        else:
            params.append(custom)

    programs = Program.objects.all().prefetch_related('pi')

    pi_names = {}
    for program in programs:
        pi_names[program.id] = program.pi.name

    context = {'cruises': cruises,
                'parameters': params,
                'pi_names': pi_names,
                'custom': "True",
                }
    return render(request, 'hydrotable/index.html', context)
