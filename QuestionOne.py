"""
Sources: 
1. Interview Cake explaining how the LRU cache is implemented
using Doubly Linked List
2. Educative.io for how to implement an LRU and illustrations of what a LRU 
cache

Explanation of Code:
Chosen Class:
From the sources I used, the best implementation seemed to be the combination 
of a hashtable and a doubly linked list. 
An orderedDict class in Python uses exactly that in the back end
All operations take O(1) time. 



"""




from collections import OrderedDict

from pyrsistent import v


class LRU_Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.cache.get(key):
            self.cache.move_to_end(key)
            return self.cache.get(key)
        return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) < self.capacity:
            self.cache.update({key: value})
        elif len(self.cache) == self.capacity:
            cache_list = list(self.cache.items())

            del cache_list[0]
            self.cache = OrderedDict(cache_list)
            self.cache.update({key:value})
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.cache)
print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
