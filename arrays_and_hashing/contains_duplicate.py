"""
LeetCode 217 - Contains Duplicate

Task:
Given an integer array `nums`, return `True` if any value appears at least twice
in the array. Otherwise, return `False`.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: True

Example 2:
Input: nums = [1, 2, 3, 4]
Output: False
"""


# Solution 1: naive O(2n) time, O(n) space
def contains_duplicate_sol1(nums: list[int]) -> bool:
    hashmap = {}

    for elem in nums:
        if elem not in hashmap.keys():
            hashmap[elem] = 1
        else: hashmap[elem] = hashmap[elem] + 1
    
    for key, value in hashmap.items():
        if value > 1:
            return True
    return False


# Solution 2: hash set iteration, O(n) space and time
def contains_duplicate_sol2(nums: list[int]) -> bool:
    hashset = set()
    for elem in nums:
        if elem in hashset:
            return True
        else:
            hashset.add(elem)
    return False


# Solution 3 O(n) space and time
def contains_duplicate_sol3(nums: list[int]) -> bool:
    if len(nums) != len(set(nums)):
        return True
    return False


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 2, 3, 3], True),          # duplicate exists
        ([1, 2, 3, 4], False),         # no duplicate
        ([1], False),                  # single element
        ([7, 7, 7], True),             # all same
        ([-1, -2, -3, -1], True),      # negative numbers
        ([1000000, -1000000, 0], False),
        ([5, 1, 2, 3, 4, 5], True),    # duplicate far apart
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, expected in test_cases:
        result = solution_func(nums[:])  # pass copy in case solution mutates input
        if result == expected:
            passed += 1
            print(f"PASS | nums={nums} -> {result}")
        else:
            print(f"FAIL | nums={nums} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")

if __name__ == "__main__":
    run_basic_tests(contains_duplicate_sol1)
    run_basic_tests(contains_duplicate_sol2)
    run_basic_tests(contains_duplicate_sol3)
    pass


# =========================
# hashset properties, set creation and add
# =========================

