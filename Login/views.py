import textwrap
import pymongo
import json
from Login.models import *

from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render, redirect

def hello(request):
    return render(request, 'Login.html')

def dispatch(request, *args, **kwargs):
    test = Test()
    testin = test.ttt()
    response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
                <p>{testin}<p>
            </body>
            </html>
        '''.format(testin=testin))
    return HttpResponse(response_text)


def Test_view(request):
    test = Test()
    test.CheckDBWrite("idunnowhatisitem", 6)
    return redirect('hello:home')