#!/usr/bin/env python3
"""This module contains the class `Cache`, and some related helper functions.
"""
import redis
from typing import Union, Callable, Optional, Any
from uuid import uuid4
from functools import wraps


def replay(fn: Callable) -> None:
    """
    replay displays the input and output history of `fn`, gotten from the
    redis cache.
    """
    if not isinstance(fn, Callable) or not hasattr(fn, "__self__"):
        return
    cache = getattr(fn.__self__, "_redis", None)
    if not isinstance(cache, redis.Redis):
        return

    call_count = cache.get(fn.__qualname__)
    if call_count is None:
        return
    try:
        call_count = int(call_count)
    except ValueError:
        return

    count_msg = "{} was called {} times:".format(fn.__qualname__, call_count)
    inputs_key = "{}:inputs".format(fn.__qualname__)
    input_history = cache.lrange(inputs_key, 0, -1)
    outputs_key = "{}:outputs".format(fn.__qualname__)
    output_history = cache.lrange(outputs_key, 0, -1)

    print(count_msg)
    for input, output in zip(input_history, output_history):
        input = input.decode("utf-8") if input is not None else input
        output = output.decode("utf-8") if output is not None else output
        print("{}(*{}) -> {}".format(fn.__qualname__, input, output))


def call_history(method: Callable) -> Callable:
    """
    call_history defines a wrapper function that stores the call input and
    output of a decorated function or method.
    """
    input_history = "{}:inputs".format(method.__qualname__)
    output_history = "{}:outputs".format(method.__qualname__)

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        wrapper stores the input and output history of the function which it
        wraps. It does this using redis.
        """
        reval = method(self, *args, **kwargs)
        if not isinstance(self._redis, redis.Redis):
            return reval

        self._redis.rpush(input_history, str(args))
        self._redis.rpush(output_history, reval)

        return reval

    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    This is a function that returns a wrapper which increments a counter
    for a given key.
    The key is gotten from the qualified name of the `method` argument.
    The wrapper returns the original return value of the `redis.get` method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """wrapper calls the `method` after it increments the redis counter.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    This is the Cache class.
    """

    def __init__(self):
        """
        This function runs when a new instance of the class is created.
        It gets the redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store generates a new key and stores `data` in redis using the key.
        It returns the key for the data.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        get returns the value of a given key converted to a specific type using
        the function `fn` if present. It otherwise return the value as is.
        """
        value = self._redis.get(key)
        return fn(value) if fn and value else value

    def get_str(self, key: str) -> Optional[str]:
        """
        get_str automatically parametizes `get` method with the correct func,
        in this case, `str`. It consequently returns a string.
        """
        return self.get(key, fn=lambda v: v.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        get_int automatically parametizes `get` method with the correct func,
        in this case, `int`. It consequently returns an int.
        """
        return self.get(key, fn=int)
