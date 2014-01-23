import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from pyzotero import zotero

from bibliography.models import Bibliography

def _get_json():
    zot = zotero.Zotero('220378' , 'group', 'xQkSPMDEBIeIjqgJsJlN8m0A')
    zot.add_parameters(itemType="-attachment")

    items = zot.everything(zot.top())
    itemlist = []

    for unit in items:
        itemlist.append({
            'label': unit.get('title', ''),
            'year': unit.get('date', ''),
            'authors': '; '.join(
                [', '.join([elem.get('lastName', None),
                elem.get('firstName', None)]) for elem in\
                unit.get('creators', {})]),
            'uri': unit.get('url', ''),
            'publisher': unit.get('publicationTitle', ''),
        })         

    exhibit_json = {
            'types': {
            "Document": {
                'pluralLabel':  "Documents",
            },
        },
        'properties': {
            #'year' : {
            #    'valueType':    "number"
            #},
            #'authors' : {
            #    'valueType':    "string"
            #},
            #'publisher' : {
            #    'valueType':    "string"
                #},
        },
        'items': itemlist,
    }

    return json.dumps(exhibit_json)


def index(request):
    return render(request, "bibliography/index.html")


def cached_bibliography(request):
    b = Bibliography.objects.all()[0]

    return HttpResponse(b, mimetype="application/json")

def load_bibliography(request):
    if len(Bibliography.objects.all()) is 0:
        b = Bibliography()
    else:
        b = Bibliography.objects.all()[0]

    b.text = _get_json()
    b.save()
    return HttpResponse('Bibliography updated succesfully')
