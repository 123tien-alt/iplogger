from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests

def get_client_ip(request):
    # Lấy IP gốc kể cả khi có proxy
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def log_ip(request):
    ip = get_client_ip(request)
    location_info = "Không xác định"

    try:
        # Gọi API lấy thông tin IP
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=query,country,regionName,city")
        data = response.json()
        if data["country"]:
            location_info = f"{data['query']} - {data['country']} ({data['city']})"
    except Exception as e:
        location_info = f"{ip} - lỗi khi lấy địa chỉ: {e}"

    # Ghi log chi tiết
    log_line = f"{datetime.datetime.now()} - {location_info}\n"
    with open("log_ip.txt", "a") as f:
        f.write(log_line)

    # Vẫn load trang iframe như cũ (ví dụ TikTok)
    return render(request, 'tracker/index.html')

def home(request):
    ip = get_client_ip(request)
    return HttpResponse(f"Chào bạn! IP của bạn là: {ip}")
