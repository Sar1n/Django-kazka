from django.urls import path, re_path
from . import views

app_name = 'MainGame'

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/AddTale/', views.AddTale, name='AddTale'),
    path('ajax/GetAddSentenceResponse/', views.GetAddSentenceResponse, name='GetAddSentenceResponse'),
    path('ajax/AddSentence/', views.AddSentence, name='AddSentence'),
    path('ajax/rfhtales/', views.rfhtales, name='rfhtales'),
    path('ajax/GetRandomResponse/', views.GetRandomResponse, name='GetRandomResponse'),
    path('ajax/CloseTale/', views.CloseTale, name='CloseTale'),
    path('ajax/CloseEdit/', views.CloseEdit, name='CloseEdit'),
]