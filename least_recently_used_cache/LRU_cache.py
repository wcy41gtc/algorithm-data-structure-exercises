# the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of
# cache in which we remove the least recently used entry when the cache memory reaches its limit.

# Your job is to use an appropriate data structure(s) to implement the cache.

# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, 
# you must write code that removes the least recently used entry first and then insert the element.
# All operations must take O(1) time.

# For the current problem, you can consider the size of cache = 5.



class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3