from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
from configs.models import Configuration, Component

def server(request: HttpRequest):
    configuration = Configuration.objects.last() # last row is always the active one
    return render(request, "configs/server.html", {"configuration": configuration})

def components(request: HttpRequest):
    componentes = Component.objects.all()
    instalados = componentes.count()
    return render(request, "configs/components.html", {"instalados": instalados, "componentes": componentes})
