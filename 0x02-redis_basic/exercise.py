#!/usr/bin/env python3
"""
This module provides a Cache class for interacting with Redis to store
data with randomly generated keys.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class to interact with a Redis data store.
    """
    
    def __init__(self):
        """
        Initialize a new Cache instance.
        Creates a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the provided data in Redis with a random key.

        Args:
            data: The data to store, which can be of type str, bytes, int, or float.

        Returns:
            A string representing the randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

