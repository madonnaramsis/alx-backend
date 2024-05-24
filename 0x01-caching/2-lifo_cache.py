#!/usr/bin/python3
"""
This module defines the BasicCache class, which is a subclass of BaseCaching.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class represents a Last-In-First-Out (LIFO) caching algorithm.

    It inherits from the BaseCaching class
    and implements the put and get methods.
    """

    def __init__(self):
        """
        Initializes a new instance of the LIFOCache class.
        """
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key to associate with the item.
            item: The item to be added to the cache.

        Returns:
            None
        """
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key,
            or None if the key is not found in the cache.
        """
        return self.cache_data.get(key)
