import requests

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()

        if "error" in data:
            return f"{ip} - Không lấy được thông tin"

        country = data.get("country_name", "Không rõ")
        region = data.get("region", "Không rõ")
        city = data.get("city", "Không rõ")

        return f"{ip} - {country} ({city}, {region})"
    except Exception as e:
        return f"{ip} - lỗi khi lấy địa chỉ: {e}"
