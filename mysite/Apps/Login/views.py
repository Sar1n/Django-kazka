import textwrap
import json
from mysite.Apps.Tales.models import *

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# authentication test >
def login(request):
  tales = [""] * 4
  for i in range (4):
    dataset = UserlessSentence.objects.all().filter(taleID=i+1)
    for obj in dataset:
      tales[i] += obj.Sentence + '. '
  context = {
        "first_tale" : tales[0],
        "second_tale" : tales[1],
        "third_tale" : tales[2],
        "fourth_tale" : tales[3],
    }
  return render(request, 'Login_prod.html', context)

@login_required
def home(request):
  #return render(request, 'MainBody.html')
  return redirect('/maingame/', permanent=True)
# authentication test <
