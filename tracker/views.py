from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .ip_lookup import get_ip_info  # 👈 Thêm dòng này

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def log_ip(request):
    ip = get_client_ip(request)
    location_info = get_ip_info(ip)  # 👈 Gọi hàm mới

    with open("log_ip.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {location_info}\n")

    return render(request, 'tracker/index.html')

def home(request):
    ip = get_client_ip(request)
    return HttpResponse(f"Chào bạn! IP của bạn là: {ip}")
