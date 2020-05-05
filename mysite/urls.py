"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Login import views as LoginViews
from Tales import views as TalesViews
from MainGame import views as MainGameViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login', views.dispatch, name='login'),
    # path('hello/', include('Login.urls', namespace='hello')),


    #path('Tales/', TalesViews.AddSentence, name="Tales"),
    path('Tales/', include("Tales.urls", namespace="Tales")),
    #path('MainGame/', MainGameViews.CreateTale, name="MainGame"),
    path('MainGame/', include("MainGame.urls", namespace="MainGame")),


    # authentication test >
    path("login1/", LoginViews.login, name="login1"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", LoginViews.home, name="home"),
    # authentication test <
]