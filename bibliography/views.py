import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from bibliography.models import Bibliography
from mendeley_client import create_client

def _get_json():

    groupId = 3511431
    config = os.path.join(os.path.dirname(__file__), 'config.json')
    mendeley = create_client(config_file=config)
    
    response = mendeley.public_group_docs(groupId, items=1)
    response = mendeley.public_group_docs(groupId, items=response['total_results'])
    all_documents = []
    for i, doc_id in enumerate(response['document_ids']):
        response = mendeley.group_doc_details(groupId, doc_id)
        all_documents.append(response)
        if i > 20:
            break

    def sort(first, second=None, reverse=False):
        """Sort group documents.

        

        """
        def get_year(doc):
            return doc.get('year', None)
        def get_author(doc):
            try:
                #return doc['authors'][0]['surname']
                return doc.get
            except KeyError, IndexError:
                return None

        def get_attribute(doc, key):
            if key == 'year':
                return get_year(doc)
            elif key == 'author':
                return get_author(doc)
            else:
                return None

        def get_key(doc):
            key = []
            key.append(get_attribute(doc, first))
            if second:
                key.append(get_attribute(doc, second))
            return tuple(key)

        return sorted(all_documents, key=get_key, reverse=reverse)
    
    sorted_doc=sort('year', 'author')

    #test = []
    #for xxx in year_author_sort:
    #    test.append([xxx['year'], xxx['authors'][0]['surname'], xxx['mendeley_url']])
    docs = []

    for doc in sorted_doc:
        docs.append({
            'label': doc['title'],
            #'type': "Document",
            'year':     doc['year'],
            'authors':  '; '.join([', '.join([elem.get('surname', None), elem.get('forename', None)]) for elem in doc['authors']]),
            'uri':      doc['mendeley_url'],
            'abstract': ' '.join(doc.get('abstract', '').split(' ')[:100]) + '...',
            'publisher' : doc.get('publication_outlet', ''),
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
        'items': docs,
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
    return HttpResponse('it worked load.json')
