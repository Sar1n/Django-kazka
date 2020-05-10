from django.shortcuts import render
from mysite.Apps.Tales.models import *
from datetime import datetime

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse


from django.template import loader


# Create your views here.

def index(request):
    data = UserlessTale.objects.all().filter(isFinished=0)
    notfin = UserlessTale.objects.all().filter(isFinished=0).count()
    fin = UserlessTale.objects.all().filter(isFinished=1).count()
    context = {
        "notfinished" : notfin,
        "finished" : fin,
        "mostauthor" : "Евгений Понасенков",
        "leastauthor" : "Вася Пупкин",
        "tales" : data,
    }
    return render(request, 'MainBody.html', context)


def GetAddSentenceResponse(request):
    if request.is_ajax():
        taleid = request.POST.get('buttonvalue')
        tale = UserlessTale.objects.all().filter(id=taleid)[0]
        lastsentence = UserlessSentence.objects.all().filter(taleID=taleid).order_by('id')[0]
        context = {
            "taletitle" : tale.TaleName,
            "talelength" : tale.Length,
            "lastsentence" : lastsentence,
            "taleid" : taleid,
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



def AddSentence(request):
    if request.is_ajax() and request.POST:
        sentence = UserlessSentence(taleID = request.POST['taleid'], dateAdded = datetime.now(), Sentence = request.POST['sentence'])
        sentence.save()
        return HttpResponse()
    else:
        raise Http404
