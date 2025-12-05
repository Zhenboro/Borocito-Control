from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('user-list/', views.user_list, name="user-list"),
    path('user-report/<str:infectado>', views.user_report, name="user-report"),
    path('user-control/', views.user_control, name="user-control"),
    path('user-control-instance/<str:infectado>', views.user_control_instance, name="user-control-instance"),
    path('telemetry/', views.telemetry, name="telemetry"),
]
