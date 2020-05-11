from django.shortcuts import render
from mysite.Apps.Tales.models import *
from datetime import datetime

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse

from django.contrib.auth.models import User

from django.template import loader

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
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
        lastsentence = UserlessSentence.objects.all().filter(taleID=taleid).order_by('-id')[0]
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
        currentuser = request.user
        if request.user.is_authenticated:
            tale = Tale(TaleName = request.POST['title'], dateStarted = datetime.now(), Length = 1, isFinished = 0, isBeingWritten = 0, lastAuthorID = currentuser)
            tale.save()
            sentence = Sentence(taleID = tale, dateAdded = datetime.now(), Sentence = request.POST['firstsentence'], authorID = currentuser)
            sentence.save()
            return HttpResponse()
        else:
            raise Http404
    else:
        raise Http404



def AddSentence(request):
    if request.is_ajax() and request.POST:
        taleid = request.POST['taleid']
        tale = UserlessTale.objects.all().filter(id=taleid)[0]
        tale.Length += 1
        tale.save()
        sentence = UserlessSentence(taleID = tale, dateAdded = datetime.now(), Sentence = request.POST['sentence'])
        sentence.save()
        return HttpResponse()
    else:
        raise Http404
