#!/usr/bin/env python3
"""This module contains the function `schools_by_topics`.
"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools with the given topic"""
    if not isinstance(topic, str):
        raise TypeError("topic must be a string")

    return mongo_collection.find({"topics": {"$elemMatch": {"$eq": topic}}})
