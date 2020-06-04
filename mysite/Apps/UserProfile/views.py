from django.shortcuts import render
from django.contrib.auth.models import User
from mysite.Apps.Tales.models import *
from datetime import datetime

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.

@login_required
def profile(request):
	currentuser = request.user
	user = User.objects.all().filter(id = currentuser.id)[0]
	participationcount = Sentence.objects.values('taleID_id').filter(authorID_id = currentuser.id).distinct().count()
	date = datetime.strftime(user.date_joined,"%d-%m-%Y")
	if (participationcount % 10 != 1) or (participationcount == 11):
		kaz = 'казках'
	else:
		kaz = 'казці'
	auth = 0
	tales = Tale.objects.values('id').distinct()
	for tale in tales:
		sent = Sentence.objects.all().filter(taleID_id = tale['id']).order_by('id')[0]
		if sent.authorID_id == currentuser.id:
			auth += 1
	if (auth % 10 != 1) or (auth == 11):
		ist = 'найкумедніших історій'
	else:
		ist = 'найкумеднішої історії'
	context = {
    "user" : user,
	"participation" : participationcount,
	"kaz" : kaz,
	"date" : date,
	"author" : auth,
	"istor" : ist
    }
	return render(request, "profile.html", context)