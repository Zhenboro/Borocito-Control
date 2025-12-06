from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json

# Create your views here.
from api.models import Instancia

# TODO : middleware para la auth

@csrf_exempt
def report(request: HttpRequest):
    if request.method == "POST":
        cuerpo = dict(json.loads(request.body))
        instancia = Instancia(**cuerpo)
        instancia.save()
    return JsonResponse({"uuid": instancia.uuid}, safe=False, status=201)

@csrf_exempt
def telemetry(request: HttpRequest):
    if request.method == "POST" and request.FILES["archivo"]:
        archivo = request.FILES["archivo"]
        # TODO : nombre del archivo debe incluir el uuid o key del que origen
        with open(f"{settings.BOROCITO_TELEMETRY_DIR}/{archivo.name}", "wb+") as destination:
            for chunk in archivo.chunks():
                destination.write(chunk)
    return JsonResponse({"status": True}, safe=False)
