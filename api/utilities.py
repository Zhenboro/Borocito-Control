from django.http import HttpRequest, JsonResponse

from configs.models import Configuration

def borocito_instance_endpoint(view_func):
    # TODO : use UUID as auth
    def wrapper(request: HttpRequest, *args, **kwargs):
        if not "User-Agent" in request.headers:
            return JsonResponse({"status": "WHO"}, status=404)
        if not "Borocito" in request.headers.get("User-Agent"):
            return JsonResponse({"status": "WHO TF ARE U LMAOOOOO"}, status=404)
        key_pairs = list(Configuration.objects.last().key_pairs)
        if not request.headers.get("Key-Pair") in key_pairs:
            return JsonResponse({"status": "NO KEY, NO PARTY."}, status=403)
        if False: # True for dev
            return JsonResponse({"status": "SUCCESS_BUT_DEV_MODE"}, status=200)
        return view_func(request, *args, **kwargs)
    return wrapper
