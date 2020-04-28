import pymongo
import json

class MongoConnector:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://MH:etozhesunrise@cluster-78bcn.gcp.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client['project']

class Test(MongoConnector):
    def CheckDBWrite(self, field, data):
        self.db.Users.insert_one({field:data})
    def ttt(self):
        d = dict((db, [collection for collection in self.client[db].collection_names()])
                for db in self.client.database_names())
        testin = json.dumps(d)
        return testin
