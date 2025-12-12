from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages

import json

# Create your views here.
from configs.models import Component

def components(request: HttpRequest):
    if request.method == "POST":
        uploaded_file = request.FILES.get('component_json_file')
        component_file = json.loads(uploaded_file.read())
        if type(component_file) == dict:
            if Component.objects.filter(name=component_file['name']).exists():
                messages.error(request, f"<b>{component_file['name']}</b> is already installed."); return redirect("configs:components")
            componente = Component(**component_file)
            componente.save()
            messages.success(request, f"<b>{componente.name}</b> by {componente.author} has been added!")
        elif type(component_file) == list:
            for componente in component_file:
                if Component.objects.filter(name=componente['name']).exists():
                    continue
                componente = Component(**componente)
                componente.save()
            messages.success(request, f"<b>{len(component_file)}</b> components has been added!")
        return redirect("configs:components")
    componentes = Component.objects.all()
    instalados = componentes.count()
    return render(request, "configs/components.html", {"instalados": instalados, "componentes": componentes})
