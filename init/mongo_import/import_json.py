#This python file uploads all JSON from the folder that should be created by the Fake_seeder
import json
import pymongo
import os
import glob
import click


def import_files(username, password):
     print (f'username', username)
     print (f'pw', password)
     try:
          client = pymongo.MongoClient(username=username, password=password, authSource='splash', authMechanism='SCRAM-SHA-256')
          #Ensure that there is a database called efrc before runing this script!!!!
          db = client.splash
          #Ensure that there exists a collection called experiments before running this script!!!!!!
          research_experiments = db.experiments
          #Ensure the JSON folder created by Fake_seeder is in the current directory
          bulk_inserts = []
          folder = os.path.dirname(os.path.realpath(__file__)) + "/Fake_Experiments/*"
          for path in glob.glob(folder):
               file = open(path, "r")
               parsed_f = json.load(file)
               bulk_inserts.append(parsed_f)
               file.close()
          #Here we insert the files into Mongodb 
          results = research_experiments.insert_many(bulk_inserts)
          print(str(results))
     except Exception as e:
          print(str(e))


@click.command()
@click.option('--username', '-u')
@click.option('--password', '-p')
def main(username=None, password=None):
     import_files(username, password)
if __name__ == '__main__':
    main()