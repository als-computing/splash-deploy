#This script creates a directory called Fake_Experiments and puts all of the fake JSON files in there,
#These will be used by import_json.py for importing to mongo
#It then creates a file called bulkfile.json which is suitable for uploading to elasticsearch using the /_bulk endpoint
import random
import json
from faker import Faker
from experiment_class import Experiment   
import uuid
    
myGenerator = Faker()

myGenerator.random.seed("Hi, there!")
random.seed(42)



research_projects = []
researchers = []
groups = []
gaps = ['1', '2', '3', 'IF']
institutions = ["UT", "UCSB"]
adsorptions = []
polymers = []

def generate_bulk_file():
    num = 0
    f = open("./bulkfile.json", "w")
    f.close()
    f = open("./bulkfile.json", "a")
    for i in research_projects:
        serialized_project = json.dumps(i.data)
        #IMPORTANT!!!!!!!!!!!! This metadata dict specifies that the JSON objects in the bulkfile is to be uploaded to the alias
        # experiments, change this if you want them to be uploaded to a different index! https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html
        metadata = {"index": {"_index": "experiments", "_id": str(num)}}
        f.write(json.dumps(metadata) + "\n")
        f.write(serialized_project + "\n")
        num+=1 
    
    f.close()


def generate_files():
    num = 0

    for i in research_projects:
        serialized_project = json.dumps(i.data, indent=4)
        f = open("./Fake_Experiments/project" + str(num) +".json", "w")
        f.write(serialized_project)
        f.close()
        num+=1 

def generate_research():
    for i in range(20):
        researchers.append({"name": myGenerator.name(), "mwet_id": str(myGenerator.uuid4())})

    for i in range(5):
        groups.append(myGenerator.last_name())

    for i in range(10):
        adsorptions.append(myGenerator.random_uppercase_letter() + myGenerator.random_lowercase_letter())

    for i in range(20):
        polymers.append(myGenerator.random_uppercase_letter() + str(myGenerator.random_digit_not_null()) + str(myGenerator.random_digit_not_null()))

    for i in range(100):
        x=Experiment()
        research_projects.append(x)
        #Avoid that whole nightmare again 
        check_for_unprofessional_lang(research_projects[i])
        researcher = random.choice(researchers)
        research_projects[i].data["researcher"]["name"] = researcher["name"]
        research_projects[i].data["researcher"]["mwet_id"] = researcher["mwet_id"] 
        research_projects[i].data["researcher"]["group"] = random.choice(groups)
        research_projects[i].data["researcher"]["institution"] = random.choice(institutions)
        research_projects[i].data["experiment_metadata"]["gap"] = random.choice(gaps)
        research_projects[i].set_polymer(random.choice(polymers))
        research_projects[i].set_adsorbing(random.choice(adsorptions))
        research_projects[i].data["uid"] = str(uuid.uuid4())

#Generate an experiment name
#Check if there's bad stuff, if there is regenerate name and check again
def check_for_unprofessional_lang(project_object):
    project_object.data["name"] = myGenerator.bs() + " tests"
    if "sexy" in project_object.data["name"]:
        check_for_unprofessional_lang(project_object)
    return




generate_research()

generate_files()

generate_bulk_file()





