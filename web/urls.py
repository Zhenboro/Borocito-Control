from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('user-list/', views.user_list, name="user-list"),
    path('user-control/', views.user_control, name="user-control"),
    path('telemetry/', views.telemetry, name="telemetry"),
]
