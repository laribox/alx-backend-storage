#!/usr/bin/env python3
"""This module contains the function `update_topics`
"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a given document"""
    if not isinstance(name, str) or not isinstance(topics, list):
        raise TypeError("name must be a string, and topics must be a list")

    if not all(isinstance(t, str) for t in topics):
        raise TypeError("topics must be a list of strings")

    try:
        mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}},
        )
    except Exception as e:
        print("failed to update many documents: {}".format(str(e)))
