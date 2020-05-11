import textwrap
import json
from mysite.Apps.Login.models import *

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#def hello(request):
 # return render(request, 'Login_prod.html')

# authentication test >
def login(request):
  return render(request, 'Login_prod.html')

@login_required
def home(request):
  return redirect('/maingame/', permanent=True)
# authentication test <

#def redirected_login(request):
 # return redirect()