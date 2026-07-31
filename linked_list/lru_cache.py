"""
LeetCode 146 - LRU Cache

Task:
Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class:
- LRUCache(capacity): initialize with positive size capacity.
- get(key): return value if key exists, otherwise -1.
- put(key, value): update or insert key-value. If insertion exceeds capacity,
  evict the least recently used key.

Both get and put should run in O(1) average time complexity.
"""


from re import S


class Node:
    #doubly linked list: easy to remove
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


# Solution 1
class LRUCacheSol1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # cache maps keys to Nodes, then node can access val
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    #helper1 
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    #helper2
    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        #idea: we use cache (hashmap) to quickly access, use linked list to keep track
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) # if in cache, remove first
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Solution 2
class LRUCacheSol2:
    def __init__(self, capacity: int):
        # TODO: write your second solution
        raise NotImplementedError("Implement LRUCacheSol2")

    def get(self, key: int) -> int:
        raise NotImplementedError("Implement get()")

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError("Implement put()")


# Solution 3 (optional)
class LRUCacheSol3:
    def __init__(self, capacity: int):
        # TODO: write your third solution (optional)
        raise NotImplementedError("Implement LRUCacheSol3")

    def get(self, key: int) -> int:
        raise NotImplementedError("Implement get()")

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError("Implement put()")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(cache_class) -> None:
    print(f"\nTesting: {cache_class.__name__}")

    # Sequence from the common LeetCode example.
    cache = cache_class(2)
    cache.put(1, 1)
    cache.put(2, 2)
    r1 = cache.get(1)          # returns 1
    cache.put(3, 3)            # evicts key 2
    r2 = cache.get(2)          # returns -1
    cache.put(4, 4)            # evicts key 1
    r3 = cache.get(1)          # returns -1
    r4 = cache.get(3)          # returns 3
    r5 = cache.get(4)          # returns 4

    got = [r1, r2, r3, r4, r5]
    expected = [1, -1, -1, 3, 4]
    if got == expected:
        print(f"PASS | got={got}")
    else:
        print(f"FAIL | got={got}, expected={expected}")


if __name__ == "__main__":
    run_basic_tests(LRUCacheSol1)
    # run_basic_tests(LRUCacheSol2)
    # run_basic_tests(LRUCacheSol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
