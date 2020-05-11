from django.urls import path, re_path
from . import views

app_name = 'Login'

urlpatterns = [
    path('', views.hello, name='home'),
]