from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_ip, name='log_ip'),
]
