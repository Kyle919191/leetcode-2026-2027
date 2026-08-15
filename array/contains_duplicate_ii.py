"""
LeetCode 219 - Contains Duplicate II

Task:
Given an integer array `nums` and an integer `k`, return `True` if there are
two distinct indices `i` and `j` in the array such that:

- `nums[i] == nums[j]`
- `abs(i - j) <= k`

Otherwise, return `False`.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: True

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: True

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: False
"""


# Solution 1
def contains_nearby_duplicate_sol1(nums: list[int], k: int) -> bool:
    left = right = 0
    window = set()

    while right < len(nums):
        elem = nums[right]
        if elem in window:
            return True
        window.add(elem)
        right += 1

        # could be if too
        while right - left > k:
            window.remove(nums[left])
            left += 1
    return False


# Solution 2
def contains_nearby_duplicate_sol2(nums: list[int], k: int) -> bool:
    # TODO: write your second solution
    raise NotImplementedError("Implement contains_nearby_duplicate_sol2")


# Solution 3 (optional)
def contains_nearby_duplicate_sol3(nums: list[int], k: int) -> bool:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement contains_nearby_duplicate_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
        ([1, 2, 3, 1], 2, False),
        ([], 0, False),
        ([1], 1, False),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, k, expected in test_cases:
        result = solution_func(nums[:], k)
        if result == expected:
            passed += 1
            print(f"PASS | nums={nums}, k={k} -> {result}")
        else:
            print(f"FAIL | nums={nums}, k={k} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(contains_nearby_duplicate_sol1)
    # run_basic_tests(contains_nearby_duplicate_sol2)
    # run_basic_tests(contains_nearby_duplicate_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
