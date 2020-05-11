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
from mysite.Apps.Login import views as LoginViews
from mysite.Apps.Tales import views as TalesViews
from mysite.Apps.MainGame import views as MainGameViews
from mysite.Apps.UserProfile import views as UserProfileViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login', views.dispatch, name='login'),
    # path('hello/', include('Login.urls', namespace='hello')),


    #path('Tales/', TalesViews.AddSentence, name="Tales"),
    #path('MainGame/', MainGameViews.CreateTale, name="MainGame"),
    path('tales/', include("mysite.Apps.Tales.urls", namespace="Tales")),
    path('maingame/', include("mysite.Apps.MainGame.urls", namespace="MainGame")),
    #path('login/', include("mysite.Apps.Login.urls", namespace="Login")),
    path('profile/', include("mysite.Apps.UserProfile.urls", namespace="UserProfile")),


    # authentication test >
    path("login/", LoginViews.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('', LoginViews.home, name="home"),
    # authentication test <
]