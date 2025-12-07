from django.urls import path
from api import views

app_name = "api"

urlpatterns = [
    path('report/', views.report, name="report"),
    path('telemetry/', views.telemetry, name="telemetry"),
    path('configuration/', views.configuration, name="configuration"),
    path('repository/', views.repository, name="repository"),
]
