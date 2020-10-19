elastic = {
    "url": "http://localhost:8080/search/",
    "alias": "run_start",
    "index_name": "splash.run_start"
}

# db = {
#    "name": "splash",
#    "collection": "experiments",
# }


# this is the configuration for the new index
# find documentation on this here
# https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html
# So far the only configuration I have done is set up autocompletion
# and keyword on select fields
INDEX_CONFIG = {
    # This setting makes it so that if a field in a document doesn't match the set datatype then
    # elastic will still index the entire document but ignore that field. This
    # doesn't work for the Nested data type, object data type, or range data type
    "settings": {"index.mapping.ignore_malformed": True},
    "mappings": {
        "properties": {
            # this is autocompletable, full text searchable, and keyword searchable
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
            # this is autocompletable, full text searchable, and keyword searchable
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
            # this is simply an integer field
            "scan_id": {
                "type": "integer"
            },
            # this is a date field which will be useful for
            # certain queries
            "time": {
                "type": "date"
            },
            # this is autocompletable, full text searchable, and keyword searchable
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
            # this is autocompletable, full text searchable, and keyword searchable
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
            # this is autocompletable, full text searchable, and keyword searchable
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
            # this is autocompletable, full text searchable, and keyword searchable
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
            # this is autocompletable, full text searchable, and keyword searchable
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
        # These templates map based on the datatype of the
        "dynamic_templates": [
            {
                # This turns the datatype long into strings when indexed
                "long_to_string": {
                    "match_mapping_type": "long",
                    "mapping": {
                        "type": "text",
                        "fields": {
                                "keyword": {
                                    "type":  "keyword",
                                    # This means that if the character count on the
                                    # text field is above 256 characters then there will
                                    # no keyword field indexed on this field
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

