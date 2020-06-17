from elastic_setup.elastic import elastic_setup
from mongo_setup import generate_json, import_json
import config


DB_NAME = config.db['name']
ALIAS = config.elastic['alias']
ELASTIC_URL = config.elastic['url']
DB_COLLECTION = config.db['collection']
ELASTIC_INDEX_NAMED_BY_MONSTACHE = config.db['name'] + "." + \
    config.db['collection']


# IMPORTANT: Elastic must be setup before Mongo
#  so that monstache can transfer the data
elastic_setup(host_url=ELASTIC_URL,
              index_name=ELASTIC_INDEX_NAMED_BY_MONSTACHE, alias=ALIAS)

generate_json.generate()

import_json.upload(db_name=DB_NAME, collection_name=DB_COLLECTION)
