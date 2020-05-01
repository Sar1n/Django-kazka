from django.urls import path, re_path
from . import views

app_name = 'Login'

urlpatterns = [
    path('', views.hello, name='home'),
    path('ajax/testadd/', views.Test_Add, name='Add'),
    path('ajax/testsubtract/', views.Test_Subtract, name='Subtract'),
    re_path(r'^testbutton$', views.Test_view, name='test'),
]