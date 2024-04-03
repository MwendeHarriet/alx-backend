#!/usr/bin/env python3
"""Module for stack caching."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class."""

    def __init__(self):
        """Function intialize."""
        super().__init__()
        self.__stack = []

    def put(self, key, item):
        """Function inserts in dict."""
        if key is None or item is None:
            return
        self.__stack.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > super().MAX_ITEMS:
            del self.cache_data[self.__stack[-2]]
            print("DISCARD: {}".format(self.__stack.pop(-2)))

    def get(self, key):
        """Function retrieves key."""
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
