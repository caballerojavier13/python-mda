from django.shortcuts import render_to_response
from django.http import HttpResponse
from pythonMDA.apps.persona.models import persona
from django.core import serializers
from django.template import RequestContext


def list_personas_view(request):

    return render_to_response('persona/list_persona.html',
                    context_instance=RequestContext(request),
                    )

def list_personas_json(request):
    data = serializers.serialize('json', persona.objects.filter())

    return HttpResponse(data,content_type='application/json; charset=utf-8')

def new_personas_view(request):

    return render_to_response('persona/new_persona.html',
                    context_instance=RequestContext(request),
                    )

def edit_personas_view(request):

    return render_to_response('persona/edit_persona.html',
                    context_instance=RequestContext(request),
                    )

def delete_personas_view(request):

    return render_to_response('persona/delete_persona.html',
                    context_instance=RequestContext(request),
                    )

