from elastic_setup.elastic import elastic_setup
# from mongo_setup import generate_json, import_json
import config


# DB_NAME = config.db['name']
# DB_COLLECTION = config.db['collection']

ALIAS = config.elastic['alias']
ELASTIC_URL = config.elastic['url']
ELASTIC_INDEX_NAMED_BY_MONSTACHE = config.elastic['index_name']


# IMPORTANT: Elastic must be setup before Mongo
#  so that monstache can transfer the data
elastic_setup(host_url=ELASTIC_URL,
              index_name=ELASTIC_INDEX_NAMED_BY_MONSTACHE,
              index_config=config.INDEX_CONFIG,
              alias=ALIAS)


# uncomment ONLY if you wish to generate fake data for mongo,
# Probably don't want to do this because it will get mixed up
# in the real data
# generate_json.generate()

# import_json.upload(db_name=DB_NAME, collection_name=DB_COLLECTION)
