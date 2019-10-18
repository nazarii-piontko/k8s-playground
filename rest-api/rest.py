import falcon
import json
import pymongo
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class DefaultResource():
    def on_get(self, req, resp):
        records = self.__get_collection().find().sort('_id', pymongo.DESCENDING).limit(10)
        resp.body = JSONEncoder().encode(list(records))

    def on_post(self, req, resp):
        self.__get_collection().insert_one({ 'data': req.bounded_stream.read().decode("utf-8") })
        resp.body = '{"status": true}'

    def __get_collection(self):
        db_client = pymongo.MongoClient("mongodb://mongodb.default.svc.cluster.local:27017")
        collection = db_client["rest"]["records"]
        return collection


app = falcon.API()
res = DefaultResource()

app.add_route('/', res)
