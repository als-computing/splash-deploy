from elasticsearch import Elasticsearch


def elastic_setup(host_url=None, index_name=None, alias=None):
    if (type(host_url) != str):
        raise TypeError("argument host_url must be of type string")
    if(type(index_name) != str):
        raise TypeError("argument index_name must be of type string")
    if(type(alias) != str):
        raise TypeError("argument index_name must be of type string")

    ELASTIC_HOST_URL = host_url

    INDEX_NAME = index_name
    ALIAS = alias
    # this is the configuration for the new index
    # find documentation on this here
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html
    # So far the only configuration I have done is set up autocompletion
    # and keyword on select fields
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
            }
        }
    }

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


INDEX_CONFIG_2 = {
    # This setting makes it so that if a field in a document doesn't match the set datatype then
    # elastic will still index the entire document but ignore that field
    "settings": {"index.mapping.ignore_malformed": True},
    "mappings": {
        "properties": {
            "project": {
                "type": "text",
                "fields": {
                    "autocomplete": {
                        "type": "completion"
                    },
                    "keyword": {
                        "type": "keyword"
                    }
                }
            },
            "sample": {
                "type": "text",
                "fields": {
                    "autocomplete": {
                        "type": "completion"
                    },
                    "keyword": {
                        "type": "keyword",
                    }
                }
            },
            "scan_id": {
                "type": "integer"
            },
            "time": {
                "type": "date"
            },
            "uid": {
                "type": "text",
                "fields": {
                    "autocomplete": {
                        "type": "completion"
                    },
                    "keyword": {
                        "type": "keyword"
                    }
                }
            },
            "group": {
                "type": "text",
                "fields": {
                    "autocomplete": {
                        "type": "completion"
                    },
                    "keyword": {
                        "type": "keyword"
                    }
                }
            },
            "owner": {
                "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                            },
                            "autocomplete": {
                                "type": "completion"
                            }
                        }
            },
            "beamline_id": {
                "type": "text",
                "fields": {
                    "autocomplete": {
                        "type": "completion"
                    },
                    "keyword": {
                        "type": "keyword"
                    }
                }
            },
            "user": {
                "type": "text",
                "fields": {
                    "autocomplete": {
                        "type": "completion"
                    },
                    "keyword": {
                        "type": "keyword"
                    }
                }
            }
        },
        "dynamic_templates": [
            {
                "long_to_string": {
                    "match_mapping_type": "long",
                    "mapping": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type":  "keyword",
                                "ignore_above": 256
                            },
                        }
                    }
                },
            },

            {
                "boolean_to_string": {
                    "match_mapping_type": "boolean",
                    "mapping": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type":  "keyword",
                                "ignore_above": 256
                            },
                        }
                    }
                },
            },

            {
                "date_to_string": {
                    "match_mapping_type": "date",
                    "mapping": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type":  "keyword",
                                "ignore_above": 256
                            },
                        }
                    }
                },
            },

            {
                "double_to_string": {
                    "match_mapping_type": "double",
                    "mapping": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type":  "keyword",
                                "ignore_above": 256
                            },
                        }
                    }
                },
            },

            {
                "strings": {
                    "match_mapping_type": "string",
                    "mapping": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type":  "keyword",
                                "ignore_above": 256
                            }
                        }
                    }
                }
            }
        ]
    },
}
