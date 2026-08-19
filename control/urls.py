from django.urls import path
from control import views

app_name = "control"

urlpatterns = [
    path('instance/<str:uuid>', views.instance, name="instance"),
    
    path('list/instances', views.list_instances, name="list-instances"),
    path('list/telemetry-logs', views.list_telemetry_logs, name="list-telemetry-logs"),
    path('list/telemetry-files', views.list_telemetry_files, name="list-telemetry-files"),
    
    path('get/report/<str:uuid>', views.get_user_report, name="get-report"),
    path('get/telemetry-log/<str:uuid>', views.get_telemetry_log, name="get-telemetry-log"),
    path('get/telemetry-file/<str:uuid>', views.get_telemetry_file, name="get-telemetry-file"),
]
