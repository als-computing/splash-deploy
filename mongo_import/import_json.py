#This python file uploads all JSON from the folder that should be created by the Fake_seeder
import json
import pymongo
import os

client = pymongo.MongoClient()

#Ensure that there is a database called efrc before runing this script!!!!
db = client.efrc

#Ensure that there exists a collection called experiments before running this script!!!!!!
research_experiments = db.experiments

#Ensure the JSON folder created by Fake_seeder is in the current directory
directory = os.fsencode("./Fake_Experiments")

bulk_inserts = []
for file in os.listdir(directory):
     path = os.path.join(directory, file)
     f = open(path, "r")
     parsed_f = json.load(f)
     bulk_inserts.append(parsed_f)
     f.close()

#Here we insert the files into Mongodb 
results = research_experiments.insert_many(bulk_inserts)

print(results)