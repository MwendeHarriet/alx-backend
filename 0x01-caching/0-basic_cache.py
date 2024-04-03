#!/usr/bin/python3
"""Module for basic caching."""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache that inherits from BaseCaching and is a caching system."""

    def __init__(self):
        """Function Initialize."""
        super().__init__()

    def put(self, key, item):
        """Function inserts in dict."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Function retrieves key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
