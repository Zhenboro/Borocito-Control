from django.http import HttpRequest, HttpResponse, JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json
import requests
from pathlib import Path
from datetime import datetime

# Create your views here.
from api.utilities import new_instance_endpoint, borocito_instance_endpoint
from api.models import Instancia, Telemetria
from configs.models import Component, Configuration

@csrf_exempt
@new_instance_endpoint
def report(request: HttpRequest):
    if request.method == "POST":
        cuerpo = dict(json.loads(request.body))
        
        # Existe, asi que solo actualizamos
        if request.headers.get("UUID"):
            instancia = Instancia.objects.filter(uuid=request.headers.get("UUID")).first()
            for campo, valor in cuerpo.items():
                setattr(instancia, campo, valor)
            instancia.public_ip = request.META.get('REMOTE_ADDR')
            instancia.save()
            return JsonResponse({"uuid": instancia.uuid}, status=200)
        
        # No existe, asi que lo creamos
        instancia = Instancia(**cuerpo)
        instancia.public_ip = request.META.get('REMOTE_ADDR')
        instancia.save()
        return JsonResponse({"uuid": instancia.uuid}, status=201)
    return JsonResponse({"status": "METHOD_NOT_SUPPORTED"}, status=405)

@csrf_exempt
@borocito_instance_endpoint
def telemetry(request: HttpRequest):
    if request.method == "POST":
        instancia = Instancia.objects.filter(uuid=request.headers.get("UUID")).first()
        if 'file' in request.FILES and request.FILES["file"]: # Es un archivo
            archivo = request.FILES["file"]
            telemetria = Telemetria(
                filename=archivo.name,
                extension=Path(archivo.name).suffix,
                size=archivo.size,
                instance=instancia,
            )
            telemetria.telemetry.save(archivo.name, archivo)
            return JsonResponse({"uuid": telemetria.uuid}, status=201)
        if request.POST.get('content'): # Es telemetria (texto plano)
            content = request.POST.get('content')
            with open(str(f"{settings.BOROCITO_TELEMETRY_DIR}/{instancia.uuid}.log"), "a", encoding="utf-8") as file:
                file.write(str(f"{content}\n"))
            return JsonResponse({"status": "OK"}, status=201)
    return JsonResponse({"status": "METHOD_NOT_SUPPORTED"}, status=405)

def configuration(request: HttpRequest):
    config = Configuration.objects.last()
    respuesta = str(f"# Borocito Configuration File\n")
    respuesta += str(f"[General]\n")
    respuesta += str(f"Enabled={config.server_status}\n")
    respuesta += str(f"FallbackServer={config.fall_back_server}\n")
    respuesta += str(f"[Borocitos]\n")
    respuesta += str(f"Version={config.borocitos['version']}\n")
    respuesta += str(f"Binaries={config.borocitos['binaries']}\n")
    respuesta += str(f"[boro-get]\n")
    respuesta += str(f"Name={config.boro_get['name']}\n")
    respuesta += str(f"Author={config.boro_get['author']}\n")
    respuesta += str(f"Website={config.boro_get['website']}\n")
    respuesta += str(f"Version={config.boro_get['version']}\n")
    respuesta += str(f"Repository={config.boro_get['repository']}\n")
    respuesta += str(f"Binaries={config.boro_get['binary']}\n")
    return HttpResponse(respuesta, content_type="plain/text")

@csrf_exempt
@borocito_instance_endpoint
def instance(request: HttpRequest):
    instancia = Instancia.objects.filter(uuid=request.headers.get("UUID")).first()
    if request.method == "POST": # send response to CS
        instancia.command = None
        instancia.response = request.POST.get('content')
        instancia.save(update_fields=['command', 'response'])
        return HttpResponse(f"OK! {instancia.uuid}", content_type="plain/text")
    elif request.method == "GET": # get commands from CS
        respuesta = str(f"#|Borocito-CS|{instancia.uuid}|{datetime.now().strftime("%H:%M:%S %d/%m/%Y")}\r\n")
        respuesta += str(f"Command1>{instancia.command or ''}\r\n")
        respuesta += str(f"Command2>\r\n")
        respuesta += str(f"Command3>\r\n")
        respuesta += str(f"[Response]\r\n")
        return HttpResponse(respuesta, content_type="plain/text")
    return JsonResponse({"status": "METHOD_NOT_SUPPORTED"}, status=405)

def repository(request: HttpRequest):
    if request.GET.get("component"):
        # TODO : controlar DoesNotExist
        component = Component.objects.get(name=request.GET.get("component"))
        if request.GET.get("download"): # not recommended
            if not component.binaries:
                return JsonResponse({"status": "BINARIES_NOT_FOUND"}, status=404)
            try:
                r = requests.get(component.binaries, stream=True)
                r.raise_for_status()
                response = StreamingHttpResponse(r.raw, content_type=r.headers.get('content-type'))
                response['Content-Disposition'] = f'attachment; filename=\"{component.name}.{request.GET.get("download")}\"'
                response['Content-Length'] = r.headers.get('content-length')
                return response
            except Exception as ex:
                return JsonResponse({"status": "SERVER_PROXY_FAIL"}, status=500)
        respuesta = str(f"# Boro-Get {component.name} Repo file\n")
        respuesta += str(f"[GENERAL]\n")
        respuesta += str(f"Author={component.author}\n")
        respuesta += str(f"From={component.website}\n")
        respuesta += str(f"[ASSEMBLY]\n")
        respuesta += str(f"Name={component.name}\n")
        respuesta += str(f"Executable={component.executable}.exe\n")
        respuesta += str(f"Version={component.version}\n")
        respuesta += str(f"Web={component.docs}\n")
        respuesta += str(f"[INSTALLER]\n")
        respuesta += str(f"Binaries={component.binaries}\n")
        return HttpResponse(respuesta, content_type="plain/text")
    config = Configuration.objects.last()
    components = Component.objects.all()
    respuesta = str(f"# Boro-Get Repository Configuration File\n")
    respuesta += str(f"[REPOSITORIES]\n")
    for component in components:
        respuesta += str(f"{component.name}={config.boro_get['repository']}?component={component.name}\n")
    return HttpResponse(respuesta, content_type="plain/text")
