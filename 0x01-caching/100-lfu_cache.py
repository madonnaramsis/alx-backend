#!/usr/bin/python3
"""
This module contains the implementation of the LFUCache class,
which is a subclass of BaseCaching.
LFUCache is a caching algorithm
that evicts the least frequently used items first.

LFUCache class has the following methods:
- __init__: Initializes an instance of LFUCache.
- put: Assigns an item to the cache.
- get: Returns the value associated with a given key from the cache.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A class that represents a Least Frequently Used (LFU) Cache.

    Attributes:
        queue (list): A list that represents the order of keys
        based on their frequency of use.
        lfu (dict): A dictionary that stores the frequency count of each key.
    """

    def __init__(self):
        """Initialize LFUCache."""
        self.queue = []
        self.lfu = {}
        super().__init__()

    def put(self, key, item):
        """Assign the item to the dictionary.

        Args:
            key: The key to be assigned.
            item: The item to be assigned.
        """
        if key and item:
            if (len(self.queue) >= self.MAX_ITEMS and
                    not self.cache_data.get(key)):
                delete = self.queue.pop(0)
                self.lfu.pop(delete)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

            if self.cache_data.get(key):
                self.queue.remove(key)
                self.lfu[key] += 1
            else:
                self.lfu[key] = 0

            insert_index = 0
            while (insert_index < len(self.queue) and
                   not self.lfu[self.queue[insert_index]]):
                insert_index += 1
            self.queue.insert(insert_index, key)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the given key.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the given key,
            or None if the key is not found.
        """
        if self.cache_data.get(key):
            self.lfu[key] += 1
            if self.queue.index(key) + 1 != len(self.queue):
                while (self.queue.index(key) + 1 < len(self.queue) and
                       self.lfu[key] >=
                       self.lfu[self.queue[self.queue.index(key) + 1]]):
                    self.queue.insert(self.queue.index(key) + 1,
                                      self.queue.pop(self.queue.index(key)))
        return self.cache_data.get(key)
