from django.shortcuts import render
from django.contrib.auth.models import User
from mysite.Apps.Tales.models import *

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile(request):
	return render(request, "profile.html")