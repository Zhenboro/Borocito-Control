from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

import json

# Create your views here.
from api.models import Instancia

# TODO : middleware para la auth

@csrf_exempt
def report(request: HttpRequest):
    if request.method == "POST":
        cuerpo = dict(json.loads(request.body))
        instancia = Instancia(**cuerpo)
        instancia.save()
    return JsonResponse({"uuid": instancia.uuid}, safe=False, status=201)

# gente, no soy experto en Django, apenas soy principiante. porfavor no me funen.
