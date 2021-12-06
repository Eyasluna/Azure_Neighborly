import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    # example call http://localhost:7071/api/getAdvertisement/?id=5eb6cb8884f10e06dc6a2084

    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            url = os.environ["mongodb://myneighborlycosmosdb:vUbZ1nPWdZv2dsSEVcJlN78zVjZl47gM81v133Mdsp6W4Oq0wKG5QwcHVzKyxcYy1HJBPDBsfRl7900BOnMTGQ==@myneighborlycosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@myneighborlycosmosdb@"]  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['myneighborlydb']
            collection = database['advertisement']
           
            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            print("----------result--------")

            result = dumps(result)
            print(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)