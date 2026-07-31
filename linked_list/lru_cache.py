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


# Solution 1
class LRUCacheSol1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()

    def get(self, key: int) -> int:
        raise NotImplementedError("Implement get()")

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError("Implement put()")


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
    # run_basic_tests(LRUCacheSol1)
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
