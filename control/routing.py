from django.urls import re_path

from control import consumers

websocket_urlpatterns = [
    re_path(r'ws/echo/$', consumers.SimpleEcho.as_asgi()),
]
