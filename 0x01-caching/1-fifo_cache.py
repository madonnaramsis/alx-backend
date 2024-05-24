#!/usr/bin/python3
"""
This module defines the BasicCache class, which is a subclass of BaseCaching.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A First-In, First-Out (FIFO) cache implementation."""

    def __init__(self):
        """
        Initializes a new instance of the FifoCache class.
        """
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache with the given key.

        Args:
            key: The key to associate with the item.
            item: The item to be added to the cache.

        Returns:
            None
        """
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the given key,
            or None if the key is not found in the cache.
        """
        return self.cache_data.get(key)
