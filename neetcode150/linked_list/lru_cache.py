"""
LeetCode 146 - LRU Cache
"""


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
        # TODO-TALK: I combine a hash map with a doubly linked list.
        # TODO-TALK: The map gives O(1) key lookup, and the list keeps usage order.
        # TODO-TALK: Left side is least recently used and right side is most recently used.
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
        # TODO-TALK: On get, missing key returns -1.
        # TODO-TALK: On hit, I move the node to most-recent position and return its value.
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # TODO-TALK: On put, I remove old node if key already exists, then insert fresh node as most recent.
        # TODO-TALK: If capacity is exceeded, I evict the least recently used node at the left boundary.
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


def run_basic_tests(cache_class) -> None:
    print(f"\nTesting: {cache_class.__name__}")
    cache = cache_class(2)
    cache.put(1, 1)
    cache.put(2, 2)
    r1 = cache.get(1)
    cache.put(3, 3)
    r2 = cache.get(2)
    cache.put(4, 4)
    r3 = cache.get(1)
    r4 = cache.get(3)
    r5 = cache.get(4)
    got = [r1, r2, r3, r4, r5]
    expected = [1, -1, -1, 3, 4]
    if got == expected:
        print(f"PASS | got={got}")
    else:
        print(f"FAIL | got={got}, expected={expected}")


if __name__ == "__main__":
    # run_basic_tests(LRUCacheSol1)
    pass
