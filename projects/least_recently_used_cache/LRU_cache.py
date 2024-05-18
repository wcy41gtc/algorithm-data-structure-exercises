# the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of
# cache in which we remove the least recently used entry when the cache memory reaches its limit.

# Your job is to use an appropriate data structure(s) to implement the cache.

# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, 
# you must write code that removes the least recently used entry first and then insert the element.
# All operations must take O(1) time.

# For the current problem, you can consider the size of cache = 5.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Hash map to store key-node pairs
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """ Remove a node from the linked list. """
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
    
    def _add(self, node):
        """Add a new node right after the head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def set(self, key, value):
        # If the capacity is 0, do nothing
        if self.capacity == 0:
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # Remove the LRU entry
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


def test():
    # Test Case 1
    cache = LRU_Cache(3)

    cache.set(1, 1)
    cache.set(2, 2)
    assert cache.get(1) == 1  # Cache hit
    assert cache.get(3) == -1  # Cache miss

    cache.set(3, 3)
    cache.set(4, 4)  # Cache is full, evicts key 2
    assert cache.get(2) == -1  # Cache miss, as key 2 was evicted
    assert cache.get(3) == 3  # Cache hit
    assert cache.get(4) == 4  # Cache hit

    print("Test Case 1 Passed")

    # Test Case 2
    cache = LRU_Cache(2)

    cache.set(1, None)  # Setting value as None
    assert cache.get(1) == None  # Cache hit, returns None

    cache.set(2, "")
    assert cache.get(2) == ""  # Cache hit, returns empty string

    cache.set(3, 3)  # Cache is full, evicts key 1
    assert cache.get(1) == -1  # Cache miss, as key 1 was evicted
    assert cache.get(2) == ""  # Cache hit, key 2 is still present

    print("Test Case 2 Passed")

    # Test Case 3
    large_value = "x" * 10**6  # 1 million characters
    cache = LRU_Cache(2)

    cache.set(1, large_value)
    assert cache.get(1) == large_value  # Cache hit, returns the large value

    cache.set(2, 2)
    assert cache.get(2) == 2  # Cache hit

    cache.set(3, 3)  # Cache is full, evicts key 1
    assert cache.get(1) == -1  # Cache miss, as key 1 was evicted
    assert cache.get(2) == 2  # Cache hit
    assert cache.get(3) == 3  # Cache hit

    print("Test Case 3 Passed")

if __name__ == "__main__":
    test()