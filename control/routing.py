from django.urls import path

from control import consumers

websocket_urlpatterns = [
    path("ws/instance/<str:uuid>/", consumers.InstanceController.as_asgi(), name="instance"),
]
