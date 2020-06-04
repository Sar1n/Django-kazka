from django.shortcuts import render
from mysite.Apps.Tales.models import *
from datetime import datetime
import random

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse

from django.contrib.auth.models import User

from django.template import loader

from django.contrib.auth.decorators import login_required

from django.template.context_processors import csrf
# Create your views here.

@login_required
def index(request):
    data = Tale.objects.all().filter(isFinished=0)
    context = {
        "tales" : data,
    }
    return render(request, 'MainBody.html', context)


def GetAddSentenceResponse(request):
    if request.is_ajax():
        taleid = request.POST.get('buttonvalue')
        if taleid != 'random':
            tale = Tale.objects.all().filter(id=taleid)[0]
            lastsentence = Sentence.objects.all().filter(taleID=taleid).order_by('-id')[0]
        else:
            B = Tale.objects.all().filter(isFinished = 0).count()
            randomid = random.randint(0, B-1)
            tales = Tale.objects.all().filter(isFinished = 0)
            tale = tales[randomid]
            lastsentence = Sentence.objects.all().filter(taleID=tale.id).order_by('-id')[0]
        context = {
                "taletitle" : tale.TaleName,
                "talelength" : tale.Length,
                "lastsentence" : lastsentence,
                "taleid" : tale.id,
            }
        return render(request, "addsentenceform.html", context)
    else:
        raise Http404
    


def AddTale(request):
    if request.is_ajax():
        currentuser = request.user
        if request.user.is_authenticated:
            title = request.POST['title']
            title = title.capitalize()
            tale = Tale(TaleName = title, dateStarted = datetime.now(), Length = 1, isFinished = 0, isBeingWritten = 0, lastAuthorID = currentuser)
            tale.save()
            sentence = Sentence(taleID = tale, dateAdded = datetime.now(), Sentence = request.POST['firstsentence'].capitalize(), authorID = currentuser)
            sentence.save()
            return HttpResponse()
        else:
            raise Http404
    else:
        raise Http404



def AddSentence(request):
    if request.is_ajax():
        currentuser = request.user
        if request.user.is_authenticated:
            taleid = request.POST['taleid']
            tale = Tale.objects.all().filter(id=taleid)[0]
            tale.lastAuthorID = currentuser
            tale.Length += 1
            tale.save()
            sentence = Sentence(taleID = tale, dateAdded = datetime.now(), Sentence = request.POST['sentence'].capitalize(), authorID = currentuser)
            sentence.save()
            return HttpResponse()
        else:
            raise Http404
    else:
        raise Http404


def rfhtales(request):
    if request.is_ajax():
        data = Tale.objects.all().filter(isFinished=0)
        context = {
        "tales" : data,
        }
        return render(request, "ListOfTales.html", context)
    else:
        raise Http404

def GetRandomResponse(request):
    if request.is_ajax():
        B = Tale.objects.all().filter(isFinished = 1).count()
        randomid = random.randint(0, B-1)
        tales = Tale.objects.all().filter(isFinished = 1)
        tale = tales[randomid]
        sentences = Sentence.objects.all().filter(taleID = tale.id).order_by('id')
        taletext = ""
        for sen in sentences:
            taletext += sen.Sentence
            if (taletext[-1] != '.'):
                taletext += '.'
            taletext += ' '
        context = {
                "title" : tale.TaleName,
                "text" : taletext,
            }
        return render(request, "randomtaleform.html", context)
    else:
        raise Http404

def CloseTale(request):
    if request.is_ajax():
        currentuser = request.user
        if request.user.is_authenticated:
            taleid = request.POST['taleid']
            tale = Tale.objects.all().filter(id=taleid)[0]
            tale.Length += 1
            tale.lastAuthorID = currentuser
            tale.isFinished = 1
            tale.dateFinished = datetime.now()
            tale.save()
            sentence = Sentence(taleID = tale, dateAdded = datetime.now(), Sentence = request.POST['sentence'].capitalize(), authorID = currentuser)
            sentence.save()
            return HttpResponse()
        else:
            raise Http404
    else:
        raise Http404