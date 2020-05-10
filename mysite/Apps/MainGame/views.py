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
    context = {
        "notfinished" : "5",
        "finished" : "1",
        "mostauthor" : "Евгений Понасенков",
        "leastauthor" : "Вася Пупкин"
    }
    return render(request, 'MainBody.html', context)


def GetAddSentenceRespose(request):
    if request.is_ajax():
        context = {
            "taleid" : request.POST.get('buttonvalue'),
            "title" : "Tale",
            "lastsentence" : "Tale last sentence"
        }
        return render(request, "addsentenceform.html", context)
    else:
        raise Http404
    


def AddTale(request):
    if request.is_ajax() and request.POST:
        tale = UserlessTale(TaleName = request.POST['title'], dateStarted = datetime.now(), Length = 1, isFinished = 0, isBeingWritten = 0)
        tale.save()
        sentence = UserlessSentence(taleID = tale, dateAdded = datetime.now(), Sentence = request.POST['firstsentence'])
        sentence.save()
        return HttpResponse()
    else:
        raise Http404



# def RetrieveTales(request):
#     if request.is_ajax():
#         tales = TestData.objects.all()
#         context = {
#             "tales" : tales,
#         }
#         return render(request, "testadd.html", context)
#     else:
#         raise Http404
