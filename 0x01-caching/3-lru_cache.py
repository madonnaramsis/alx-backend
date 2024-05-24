#!/usr/bin/env python3
"""
This module contains the LRUCache class which represents an object
that allows storing and retrieving items from a dictionary
with a LRU removal mechanism when the limit is reached.
"""

from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Represents an object that allows storing
    and retrieving items from a dictionary with a LRU
    removal mechanism when the limit is reached.

    Attributes:
        cache_data (OrderedDict): A dictionary-like object
        that stores the cache data.

    Methods:
        __init__(): Initializes the cache.
        put(key, item): Adds an item in the cache.
        get(key): Retrieves an item by key.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key: The key of the item to be added.
            item: The item to be added.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
