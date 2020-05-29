# This python file uploads all JSON from the folder
# that should be created by the Fake_seeder
import json
import pymongo
import os
import glob


def upload(db_name=None, collection_name=None):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    if (type(db_name) != str):
        raise TypeError("argument db_name must be string")
    if (type(collection_name) != str):
        raise TypeError("argument collection_name must be string")
    db = myclient[db_name]

    experiments = db[collection_name]

# Ensure the JSON folder created by Fake_seeder is in the current directory

    bulk_inserts = []
    folder = os.path.dirname(os.path.realpath(__file__)) + \
        "/Fake_Experiments/*"
    for path in glob.glob(folder):
        file = open(path, "r")
        parsed_f = json.load(file)
        bulk_inserts.append(parsed_f)
        file.close()

# Here we insert the files into Mongodb
        results = experiments.insert_many(bulk_inserts)

        print(str(results))
