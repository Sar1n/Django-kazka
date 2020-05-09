import textwrap
import json
from mysite.Apps.Login.models import *

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse

def hello(request):
  return render(request, 'Login_prod.html')

# def dispatch(request, *args, **kwargs):
#     test = Test()
#     testin = test.ttt()
#     response_text = textwrap.dedent('''\
#             <html>
#             <head>
#                 <title>Greetings to the world</title>
#             </head>
#             <body>
#                 <h1>Greetings to the world</h1>
#                 <p>Hello, world!</p>
#                 <p>{testin}<p>
#             </body>
#             </html>
#         '''.format(testin=testin))
#     return HttpResponse(response_text)


# def Test_view(request):
#     test = Test()
#     test.CheckDBWrite("idunnowhatisitem", 6)
#     return HttpResponse()

# def Test_Add(request):
#     #if request.is_ajax() and request.POST:
#         test = Test()
#         test.CheckDBWrite("testing adding", 6)
#         return HttpResponse()
#     #else:
#         #raise Http404

# def Text_Add(request):
#     textdata = request.POST['textdata']
#     text = AddingText()
#     text.DBWrite(textdata)
#     #if request.is_ajax() and request.POST:
#         #req = request.POST
#         #textdata = req.cleaned_data
#         #text = AddingText()
#         #text.DBWrite(textdata)
#     return HttpResponse()
#     #else:
#         #raise Http404

# def Text_Reveal(request):
#     text = AddingText()
#     x = text.DBGet()
#     response = {}
#     response['result'] = x
#     return HttpResponse(x)



# def Test_Subtract(request):
#     if request.is_ajax() and request.POST:
#         test = Test()
#         test.CheckDBWrite("testing substracting", 6)
#         return HttpResponse()
#     else:
#         raise Http404

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# authentication test >
def login(request):
  return render(request, 'login1.html')

@login_required
def home(request):
  return render(request, 'MainBody.html')
# authentication test <