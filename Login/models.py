import json

# class MongoConnector:
#     def __init__(self):
#         self.client = pymongo.MongoClient("mongodb+srv://MH:etozhesunrise@cluster-78bcn.gcp.mongodb.net/test?retryWrites=true&w=majority")
#         self.db = self.client['project']

# class Test(MongoConnector):
#     def CheckDBWrite(self, field, data):
#         self.db.Users.insert_one({field:data})
#     def ttt(self):
#         d = dict((db, [collection for collection in self.client[db].collection_names()])
#                 for db in self.client.database_names())
#         testin = json.dumps(d)
#         return testin


# class AddingText(MongoConnector):
#     def DBWrite(self, data):
#         self.db.Tales.insert_one({"1":data})
#     def DBGet(self):
#         Tales = self.db["Tales"]
#         x = Tales.find({"_id":ObjectId('5eac68606e85a5d630614333')})
#         #x = Tales.find(ObjectId('5eac68606e85a5d630614333'))
#         return x