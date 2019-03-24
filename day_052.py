# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:
# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
# get(key): gets the value at key. If no such key exists, return null.

import collections
class LRU:
    def __init__(self, size):
        self.size = size
        self.lruCache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.lruCache.pop(key)
            self.lruCache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.lruCache.pop(key)
        except KeyError:
            if len(self.lruCache) >= self.size:
                self.lruCache.popitem(last=False)
        self.lruCache[key] = value