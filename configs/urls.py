from django.urls import path
from configs import views

app_name = "configs"

urlpatterns = [
    path('', views.server, name="server"),
    path('components/', views.components, name="components"),
]
