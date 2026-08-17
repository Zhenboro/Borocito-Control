from django.http import HttpRequest, JsonResponse

from configs.models import Configuration

def new_instance_endpoint(view_func):
    def wrapper(request: HttpRequest, *args, **kwargs):
        if not "User-Agent" in request.headers:
            return JsonResponse({"status": "WHO"}, status=404)
        if not "Borocito" in request.headers.get("User-Agent"):
            return JsonResponse({"status": "WHO TF ARE U LMAOOOOO"}, status=404)
        key_pairs = list(Configuration.objects.last().key_pairs)
        if not request.headers.get("Key-Pair") in key_pairs:
            return JsonResponse({"status": "NO KEY, NO PARTY."}, status=403)
        return view_func(request, *args, **kwargs)
    return wrapper

def borocito_instance_endpoint(view_func):
    def wrapper(request: HttpRequest, *args, **kwargs):
        if not "User-Agent" in request.headers:
            return JsonResponse({"status": "WHO"}, status=404)
        if not "Borocito" in request.headers.get("User-Agent"):
            return JsonResponse({"status": "WHO TF ARE U LMAOOOOO"}, status=404)
        if not "UUID" in request.headers:
            return JsonResponse({"status": "BE NICE, I DONT LIKE NERD PEOPLE"}, status=404)
        return view_func(request, *args, **kwargs)
    return wrapper
