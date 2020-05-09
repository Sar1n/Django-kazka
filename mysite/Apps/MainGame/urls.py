from django.urls import path, re_path
from . import views

app_name = 'MainGame'

urlpatterns = [
    path('', views.CreateTale, name='CreateTale'),
    path('ajax/create/', views.AddTale, name='create'),
    path('ajax/retrieve/', views.RetrieveTales, name='retrieve'),
    path('ajax/GetAddSentenceRespose/', views.GetAddSentenceRespose, name='GetAddSentenceRespose'),
    #path('ajax/retrieve/', views.RetrieveTales, name='retrieve'),
]