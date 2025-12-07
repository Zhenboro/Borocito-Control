from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json
from pathlib import Path

# Create your views here.
from api.models import Instancia, Telemetria
from configs.models import Component, Configuration

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
        telemetria = Telemetria(
            filename=archivo.name,
            extension=Path(archivo.name).suffix,
            size=archivo.size,
            #instance="" # TODO
        )
        telemetria.telemetry.save(archivo.name, archivo)
        return JsonResponse({"status": True}, safe=False, status=201)
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
