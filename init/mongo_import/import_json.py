#This python file uploads all JSON from the folder that should be created by the Fake_seeder
import json
import pymongo
import os
import glob

client = pymongo.MongoClient()

#Ensure that there is a database called efrc before runing this script!!!!
db = client.splash

#Ensure that there exists a collection called experiments before running this script!!!!!!
experiments = db.experiments

#Ensure the JSON folder created by Fake_seeder is in the current directory

bulk_inserts = []
folder = os.path.dirname(os.path.realpath(__file__)) + "/Fake_Experiments/*"
for path in glob.glob(folder):
     file = open(path, "r")
     parsed_f = json.load(file)
     bulk_inserts.append(parsed_f)
     file.close()

#Here we insert the files into Mongodb 
results = experiments.insert_many(bulk_inserts)

print(str(results))
