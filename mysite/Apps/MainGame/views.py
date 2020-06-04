from django.shortcuts import render
from mysite.Apps.Tales.models import *
from datetime import datetime
import random
import collections

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
            if tale.isBeingWritten == 0:
                lastsentence = Sentence.objects.all().filter(taleID=taleid).order_by('-id')[0]
            else:
                return render(request, "beignwritten.html")
        else:
            B = Tale.objects.all().filter(isFinished = 0, isBeingWritten = 0).count()
            randomid = random.randint(0, B-1)
            tales = Tale.objects.all().filter(isFinished = 0, isBeingWritten = 0)
            tale = tales[randomid]
            lastsentence = Sentence.objects.all().filter(taleID=tale.id).order_by('-id')[0]
        tale.isBeingWritten = 1
        tale.save()
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
            tale.isBeingWritten = 0
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
            if (taletext[-1] != '.') or (taletext[-1] != '!') or (taletext[-1] != '?'):
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

def CloseEdit(request):
    if request.is_ajax():
        taleid = request.POST['taleid']
        tale = Tale.objects.all().filter(id = taleid)[0]
        tale.isBeingWritten = 0
        tale.save()
        return HttpResponse()
    else:
        raise Http404

def ShowStatistics(request):
    if request.is_ajax():
        not_complete = Tale.objects.all().filter(isFinished=0).count()
        complete = Tale.objects.all().count() - not_complete

        tales = Tale.objects.values('id').distinct()
        authors = []
        for tale in tales:
            sent = Sentence.objects.values('id', 'authorID_id').filter(taleID_id = tale['id']).order_by('id')[0]
            authors.append(sent['authorID_id'])
        mostauthor = collections.Counter(authors).most_common()[0][0]
        leastauthor = collections.Counter(authors).most_common()[-1][0]
        mosthowmuch = collections.Counter(authors).most_common()[0][1]
        leasthowmuch = collections.Counter(authors).most_common()[-1][1]
        mostauthorname = User.objects.values('first_name', 'last_name').filter(id = mostauthor)[0]
        mostauthornamesurname = mostauthorname['first_name'] + " " + mostauthorname['last_name']
        leastauthorname = User.objects.values('first_name', 'last_name').filter(id = leastauthor)[0]
        leastauthornamesurname = leastauthorname['first_name'] + " " + leastauthorname['last_name']

        ten_fift = 0
        sixt_twen = 0
        twen_thir = 0
        thir_fift = 0
        fift_plus = 0
        tales = Tale.objects.values('id').filter(isFinished=1).distinct()
        for tale in tales:
            sentcount = Sentence.objects.values('id').filter(taleID_id = tale['id']).count()
            if sentcount < 16:
                ten_fift += 1
            else:
                if sentcount < 21:
                    sixt_twen += 1
                else:
                    if sentcount < 31:
                        twen_thir += 1
                    else:
                        if sentcount < 51:
                            thir_fift += 1
                        else:
                            fift_plus += 1

        context = {
            "not_complete" : not_complete,
            "complete" : complete,
            "ten_fift" : ten_fift,
            "sixt_twen" : sixt_twen,
            "twen_thir" : twen_thir,
            "thir_fift" : thir_fift,
            "fift_plus" : fift_plus,
            "mostauthor" : mostauthornamesurname,
            "leastauthor" : leastauthornamesurname,
            "mosthowmuch" : mosthowmuch,
            "leasthowmuch" : leasthowmuch,
        }
        return render(request, "statistics.html", context)
    else:
        raise Http404