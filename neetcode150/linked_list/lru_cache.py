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
        self.capacity = capacity
        # TODO-TALK: The map gives O(1) access from key to node.
        self.cache = {} # cache maps keys to Nodes, then node can access val
        self.left = Node()
        self.right = Node()

        # TODO-TALK: Left boundary is least recent and right boundary is most recent.
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
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # TODO-TALK: Access makes this key most recently used, so I move it to the right side.
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # TODO-TALK: Existing key gets refreshed, so I remove the old node first.
            self.remove(self.cache[key]) # if in cache, remove first
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            # TODO-TALK: If over capacity, I evict from left because that is least recently used.
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
