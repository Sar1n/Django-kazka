from django.urls import path, re_path
from . import views

app_name = 'Tales'

urlpatterns = [
    path('', views.tales, name='tales'),
]