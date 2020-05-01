from django.urls import path, re_path
from . import views

app_name = 'Login'

urlpatterns = [
    path('', views.hello, name='home'),
    path('ajax/testadd/', views.Test_Add, name='Add'),
    path('ajax/textadd/', views.Text_Add, name='TextAdd'),
    path('ajax/textreveal/', views.Text_Reveal, name='TextReveal'),
    re_path(r'^testbutton$', views.Test_view, name='test'),
]