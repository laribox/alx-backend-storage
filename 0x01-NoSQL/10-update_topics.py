#!/usr/bin/env python3
"""This module contains the function `insert_school`
"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name
    """
    if not isinstance(name, str) or not isinstance(topics, list):
        raise TypeError("name must be a string, and topics must be a list")

    if not all(isinstance(t, str) for t in topics):
        raise TypeError("topics must be a list of strings")

    mongo_collection.update_many({"name":name},{"$set":{"topics",topics}});
