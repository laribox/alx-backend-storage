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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve the data stored in Redis by key and apply a conversion function if provided.

        Args:
            key: The Redis key string to retrieve.
            fn: An optional callable to convert the data to the desired format.

        Returns:
            The stored data, converted by the callable if provided, or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis by key.

        Args:
            key: The Redis key string to retrieve.

        Returns:
            The stored string or None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis by key.

        Args:
            key: The Redis key string to retrieve.

        Returns:
            The stored integer or None if the key does not exist.
        """
        return self.get(key, lambda d: int(d))
