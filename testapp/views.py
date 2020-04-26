import textwrap
import pymongo
import json

from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

def hello(request):
    return HttpResponse("HELLO")

def dispatch(request, *args, **kwargs):
   
    client = pymongo.MongoClient('mongodb://MH:etozhesunrise@cluster-shard-00-00-78bcn.gcp.mongodb.net:27017,cluster-shard-00-01-78bcn.gcp.mongodb.net:27017,cluster-shard-00-02-78bcn.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster-shard-0&authSource=admin&retryWrites=true&w=majority')
    d = dict((db, [collection for collection in client[db].collection_names()])
             for db in client.database_names())
    testin = json.dumps(d)
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
