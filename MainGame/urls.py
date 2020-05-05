from django.urls import path, re_path
from . import views

app_name = 'MainGame'

urlpatterns = [
    path('', views.CreateTale, name='CreateTale'),
    path('ajax/Create/', views.AddTale, name='Create'),
]