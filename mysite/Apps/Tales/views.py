from django.shortcuts import render
from mysite.Apps.Tales.models import *

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse


# Create your views here.


def AddSentence(request):
    return render(request, 'AddSentence.html')