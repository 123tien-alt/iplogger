from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest
import datetime

def get_client_ip(request: HttpRequest):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def log_ip(request):
    ip = get_client_ip(request)
    with open("log_ip.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - IP: {ip}\n")
    return render(request, 'tracker/index.html')
from django.http import HttpResponse

def home(request):
    ip = get_client_ip(request)
    print(f"📡 IP truy cập: {ip}")
    return HttpResponse(f"Chào bạn! IP của bạn là: {ip}")

def get_client_ip(request):
    # Lấy IP gốc kể cả khi có proxy
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip