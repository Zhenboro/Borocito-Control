from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
from configs.models import Component

def components(request: HttpRequest):
    componentes = Component.objects.all()
    instalados = componentes.count()
    return render(request, "configs/components.html", {"instalados": instalados, "componentes": componentes})
