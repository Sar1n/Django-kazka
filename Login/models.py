import pymongo
import json

class Test:
    def ttt(self):
        client = pymongo.MongoClient("mongodb+srv://MH:etozhesunrise@cluster-78bcn.gcp.mongodb.net/test?retryWrites=true&w=majority")
        d = dict((db, [collection for collection in client[db].collection_names()])
             for db in client.database_names())
        testin = json.dumps(d)
        return testin
