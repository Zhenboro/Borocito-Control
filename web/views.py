from django.shortcuts import render

# Create your views here.
import requests

def dashboard(request):
    return render(request, "web/dashboard.html")

def user_list(request):
    return render(request, "web/user_list.html", {"infectados": [
        "user1",
        "user2",
        "user3",
        "user4",
    ]})

def user_control(request):
    return render(request, "web/user_control.html", {"infectados": [
        "user1",
        "user2",
        "user3",
        "user4",
    ]})

def telemetry(request):
    return render(request, "web/telemetry.html", {"archivos": [
        ["asd1.log", "27KB", ".LOG", "user1", "now"],
        ["asd2.txt", "8KB", ".TXT", "user3", " 3 hours ago"],
        ["asd3.zip", "2GB", ".ZIP", "user2", " 1 day ago"],
        ["asd4.jpeg", "1MB", ".JPEG", "user4", " 3 days ago"],
    ]})
