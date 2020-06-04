from django.urls import path, re_path
from . import views

app_name = 'Tales'

urlpatterns = [
    path('', views.index, name='index'), 
    path('author', views.authorindex, name='authorindex'), 
    path('ajax/GetTale/', views.GetTale, name='GetTale'),
]