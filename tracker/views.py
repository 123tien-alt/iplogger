from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_list = x_forwarded_for.split(',')
        for ip in ip_list:
            if ip.strip() != '127.0.0.1':
                return ip.strip()
    return request.META.get('REMOTE_ADDR')

def log_ip(request):
    ip = get_client_ip(request)
    location_info = "Không xác định"

    try:
        # Gọi API ipapi.co lấy thông tin IP
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        if 'error' not in data:
            location_info = f"{data.get('ip', ip)} - {data.get('country_name', '')} ({data.get('city', '')})"
        else:
            location_info = f"{ip} - Lỗi khi lấy thông tin: {data.get('reason')}"
    except Exception as e:
        location_info = f"{ip} - Lỗi khi gọi API: {e}"

    # Ghi log chi tiết
    log_line = f"{datetime.datetime.now()} - {location_info}\n"
    with open("log_ip.txt", "a") as f:
        f.write(log_line)

    return render(request, 'tracker/index.html')

def home(request):
    ip = get_client_ip(request)
    return HttpResponse(f"Chào bạn! IP của bạn là: {ip}")
