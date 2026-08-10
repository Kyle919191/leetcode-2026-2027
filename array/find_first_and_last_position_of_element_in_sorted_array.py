"""
LeetCode 34 - Find First and Last Position of Element in Sorted Array

Task:
Given an array of integers `nums` sorted in non-decreasing order, find the
starting and ending position of a given `target` value.

If `target` is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""


from binary_search import left_bound, right_bound


# Solution 1
def search_range_sol1(nums: list[int], target: int) -> list[int]:
    left = left_bound(nums, target)
    if left == -1:
        return [-1, -1]
    right = right_bound(nums, target)
    return [left, right]


# Solution 2
def search_range_sol2(nums: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement search_range_sol2")


# Solution 3 (optional)
def search_range_sol3(nums: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement search_range_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([1], 2, [-1, -1]),
        ([2, 2], 2, [0, 1]),
        ([1, 2, 3, 3, 3, 4, 5], 3, [2, 4]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, target, expected in test_cases:
        result = solution_func(nums[:], target)
        if result == expected:
            passed += 1
            print(f"PASS | nums={nums}, target={target} -> {result}")
        else:
            print(
                f"FAIL | nums={nums}, target={target} -> got {result}, "
                f"expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(search_range_sol1)
    # run_basic_tests(search_range_sol2)
    # run_basic_tests(search_range_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
