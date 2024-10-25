#!/usr/bin/env python3
"""This module contains the function `list_all`
"""


def list_all(mongo_collection):
    """Returns a list of all the documents in a collection"""
    return mongo_collection.find({})
