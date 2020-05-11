from django.urls import path, re_path
from . import views

app_name = 'UserProfile'

urlpatterns = [
	path('', views.profile, name='index'),
]