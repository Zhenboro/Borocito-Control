from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.conf import settings

import json

# Create your views here.
from api.models import Instancia
from configs.models import Component, Configuration

# TODO : middleware para la auth

@csrf_exempt
def report(request: HttpRequest):
    if request.method == "POST":
        cuerpo = dict(json.loads(request.body))
        instancia = Instancia(**cuerpo)
        instancia.save()
        return JsonResponse({"uuid": instancia.uuid}, safe=False, status=201)

@csrf_exempt
def telemetry(request: HttpRequest):
    if request.method == "POST" and request.FILES["archivo"]:
        archivo = request.FILES["archivo"]
        # TODO : nombre del archivo debe incluir el uuid o key del que origen
        # TODO : abstraer archivos de telemetria en un modelo ?????????????????????????
        with open(f"{settings.BOROCITO_TELEMETRY_DIR}/{archivo.name}", "wb+") as destination:
            for chunk in archivo.chunks():
                destination.write(chunk)
    return JsonResponse({"status": True}, safe=False)

def configuration(request: HttpRequest):
    config = Configuration.objects.values(
        'server_status',
        'fall_back_server',
        'borocitos',
        'boro_get',
    ).last()
    return JsonResponse(config, safe=False)

def repository(request: HttpRequest):
    components = Component.objects.all()
    repos = {}
    for component in components:
        repos.update({component.name: {
            "name": component.name,
            "executable": component.executable,
            "version": component.version,
            "binaries": component.binaries,
        }})
    return JsonResponse(repos, safe=False)
