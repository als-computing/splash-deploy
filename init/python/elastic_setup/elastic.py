from elasticsearch import Elasticsearch


def elastic_setup(host_url=None, index_name=None, index_config=None, alias=None):
    if (type(host_url) != str):
        raise TypeError("argument host_url must be of type string")
    if(type(index_name) != str):
        raise TypeError("argument index_name must be of type string")
    if(type(alias) != str):
        raise TypeError("argument alias must be of type string")
    if (type(index_config) != dict):
        raise TypeError("argument index_config must be of type dict")

    ELASTIC_HOST_URL = host_url

    INDEX_NAME = index_name
    ALIAS = alias
    INDEX_CONFIG = index_config

    # Connect with elastic
    es = Elasticsearch([ELASTIC_HOST_URL])

    # create an index
    es.indices.create(index=INDEX_NAME, body=INDEX_CONFIG)

    # This will allow us to set an alias for the index.
    # This is so that no matter what the actual index name is, the client code
    # can always refer to the same url endpoint. We have associated the alias
    # experiments, with the index name
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-aliases.html
    # https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.client.IndicesClient.put_alias

    es.indices.put_alias(index=INDEX_NAME, name=ALIAS)
