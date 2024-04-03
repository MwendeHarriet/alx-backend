#!/usr/bin/env python3
"""Module for queue caching."""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class."""

    def __init__(self):
        """Function intialize."""
        super().__init__()
        self.__queue = []

    def put(self, key, item):
        """Function inserts in dict."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.__queue.remove(key)
            self.__queue.append(key)
            self.cache_data[key] = item
            return
        self.__queue.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > super().MAX_ITEMS:
            del self.cache_data[self.__queue[0]]
            print("DISCARD: {}".format(self.__queue.pop(0)))

    def get(self, key):
        """Function retrieves key."""
        if key not in self.cache_data or key is None:
            return None
        self.__queue.remove(key)
        self.__queue.append(key)
        return self.cache_data.get(key)
