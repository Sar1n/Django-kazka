from django.urls import path, re_path
from . import views
from . import models

app_name = 'Login'

urlpatterns = [
    path('', views.hello, name='home'),
    re_path(r'^testbutton$', views.Test_view, name='test'),
]