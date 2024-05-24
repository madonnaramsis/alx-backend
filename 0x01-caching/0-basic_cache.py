#!/usr/bin/python3
"""
This module defines the BasicCache class, which is a subclass of BaseCaching.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class inherits from BaseCaching
    and represents a basic cache implementation.

    Methods:
        put(key, item): Assigns the item to the cache dictionary.
        get(key): Returns the value associated
                with the given key from the cache dictionary.
    """
    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value associated with the given key """
        return self.cache_data.get(key)
