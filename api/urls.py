from django.urls import path
from api import views

app_name = "api"

urlpatterns = [
    path('report/', views.report, name="report"), # Instances will report themselves to this endpoint
    path('telemetry/', views.telemetry, name="telemetry"), # Instances will send telemetry to this endpoint
    path('configuration/', views.configuration, name="configuration"), # Instances will configure themselves to this endpoint
    path('instance/', views.instance, name="instance"), # Instances will comunicate on this endpoint

    path('boro-get/repository', views.repository, name="repository"), # boro-get will use this endpoint for stuff
]
