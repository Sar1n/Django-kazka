from django.shortcuts import render
from mysite.Apps.Tales.models import *
from datetime import datetime

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse


from django.template import loader


# Create your views here.

def CreateTale(request):
    return render(request, 'MainBody.html')
    


def AddTale(request):
    if request.is_ajax() and request.POST:
        tale = TestData(dateStarted = datetime.now(), TaleName = request.POST['textdata'])
        #Заполняем поля чисто для не null значений
        tale.length = 0
        tale.isFinished = 0
        tale.save()
        return HttpResponse()
    else:
        raise Http404



def RetrieveTales(request):
    if request.is_ajax():
        tales = TestData.objects.all()
        context = {
            "tales" : tales,
        }
        return render(request, "testadd.html", context)
    else:
        raise Http404
