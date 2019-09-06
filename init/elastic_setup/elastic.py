from elasticsearch import Elasticsearch, exceptions

ELASTIC_HOST_URL = "localhost:80/search/"

#ATTENTION!!!!!! This must match the name that will be used
#by monstache which in turn is derived from the mongo collection name
#the naming schema goes as such: [database_name].[collection_name], for example say 
#we had a collection named 'experiments', and this collection was in a database called 'efrc'
#the index name monstache will use is 'splash.experiments'
#https://rwynn.github.io/monstache-site/start/
INDEX_NAME = "splash.experiments"

#this is the configuration for the new index
#find documentation on this here https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html
#So far the only configuration I have done is set up autocompletion and keyword on select fields
INDEX_CONFIG = {
  "mappings": {
    "properties": {
      "name": {
        "type": "text",
        "fields": {
          "autocomplete": {
            "type": "completion"
          },
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "researcher": {
        "properties": {
          "group": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              },
              "autocomplete": {
                "type": "completion"
              }
            }
          },
          "institution": {
            "type": "text",
            "fields": {
              "autocomplete": {
                "type": "completion"
              },
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "name": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              },
              "autocomplete": {
                "type": "completion"
              }
            }
          }
        }
      },
      "trials": {
        "properties": {
            "membrane_or_polymer": {
            "type": "text",
            "fields": {
                "autocomplete": {
                "type": "completion"
                },
                "keyword": {
                "type": "keyword",
                "ignore_above": 256
                }
            }
            },
            "solutes_present": {
            "type": "text",
            "fields": {
                "autocomplete": {
                "type": "completion"
                },
                "keyword": {
                "type": "keyword",
                "ignore_above": 256
                }
            }
            }
        }
      }
    }
  }
}



#Connect with elastic
es = Elasticsearch(hosts=[ELASTIC_HOST_URL])

#create an index
es.indices.create(index=INDEX_NAME, body=INDEX_CONFIG)

#This will allow us to set an alias for the index.
#This is so that no matter what the actual index name is, the client code can
#always refer to the same url endpoint. We have associated the alias
#research_experiments, with the index name
#https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-aliases.html
#https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.client.IndicesClient.put_alias
 
es.indices.put_alias(index=INDEX_NAME, name="research_experiments")

