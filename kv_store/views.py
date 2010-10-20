from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from models import KeyValueStore
import simplejson

@login_required
def store_value(request):
    for key in request.POST.keys():
        dbkey = "%s:%s" % (request.user.id, key)
        try:
            kvs = KeyValueStore.objects.get(key=dbkey)
            kvs.value = request.POST[key]
            kvs.save()
        except KeyValueStore.DoesNotExist:
            KeyValueStore.objects.create(key=dbkey, value=request.REQUEST[key])
    return HttpResponse('success')

@login_required
def retrieve_value(request):
    to_lookup = []
    for key in request.GET.keys():
        to_lookup.append("%s:%s" % (request.user.id, key))
    to_json = dict([(t.key, t.value) for t in KeyValueStore.objects.in_bulk(to_lookup).values()])
    return HttpResponse(simplejson.dumps(to_json), content_type='application/json')
