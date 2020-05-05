from django.shortcuts import render
from Tales.models import *
from datetime import datetime

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse


# Create your views here.

def CreateTale(request):
    return render(request, 'AddNewTale.html')
    


def AddTale(request):
    tale = TestData()
    now = datetime.now()
    tale.dateStarted = now
    tale.TaleName = request.POST['textdata']

    #Заполняем поля чисто для не null значений
    tale.length = 0
    tale.isFinished = 0
    #tale.lastAuthorID = 17
    
    tale.save()
    
    return HttpResponse()
