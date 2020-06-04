from django.shortcuts import render
from .models import *

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse


# Create your views here.


def index(request):
    currentuser = request.user
    alltales = Tale.objects.all().filter(isFinished=1).order_by('-dateFinished')

    b = Sentence.objects.values('taleID_id').filter(authorID_id = currentuser.id).distinct()
    membertales = Tale.objects.all().filter(id__in=b, isFinished = 1).order_by('-dateFinished')

    d = []
    tales = Tale.objects.values('id').distinct()
    for tale in tales:
        sent = Sentence.objects.values('authorID_id').filter(taleID_id = tale['id']).order_by('id')[0]
        if sent['authorID_id'] == currentuser.id:
            d.append(tale['id'])
    authortales = Tale.objects.all().filter(id__in=d, isFinished = 1).order_by('-dateFinished')

    context = {
        "alltales" : alltales,
        "membertales" : membertales,
        "authortales" : authortales,
        "author" : "",
        "member" : "active",
    }
    return render(request, 'tales.html', context)

def authorindex(request):
    currentuser = request.user
    alltales = Tale.objects.all().filter(isFinished=1)

    b = Sentence.objects.values('taleID_id').filter(authorID_id = currentuser.id).distinct()
    membertales = Tale.objects.all().filter(id__in=b, isFinished = 1)

    d = []
    tales = Tale.objects.values('id').distinct()
    for tale in tales:
        sent = Sentence.objects.values('authorID_id').filter(taleID_id = tale['id']).order_by('id')[0]
        if sent['authorID_id'] == currentuser.id:
            d.append(tale['id'])
    authortales = Tale.objects.all().filter(id__in=d, isFinished = 1)

    context = {
        "alltales" : alltales,
        "membertales" : membertales,
        "authortales" : authortales,
        "author" : "show active",
        "member" : "",
    }
    return render(request, 'tales.html', context)

def GetTale(request):
    if request.is_ajax():
        taleid = request.POST['taleid']
        tale = Tale.objects.all().filter(id=taleid)[0]
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
        return render(request, "taleform.html", context)
    else:
        raise Http404