"""
LeetCode 1 - Two Sum

Task:
Given an array of integers `nums` and an integer `target`, return indices of
the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you may not use
the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""


# Solution 1
def two_sum_sol1(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Solution 2
def two_sum_sol2(nums: list[int], target: int) -> list[int]:
    index_by_value = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in index_by_value:
            return [index_by_value[need], i]
        index_by_value[x] = i
    return []


# Solution 3 (optional)
def two_sum_sol3(nums: list[int], target: int) -> list[int]:
    index_by_value: dict[int, int] = {}
    for i, x in enumerate(nums):
        index_by_value[x] = i

    for i, x in enumerate(nums):
        need = target - x
        if need in index_by_value and index_by_value[need] != i:
            return [i, index_by_value[need]]
    return []


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, target, expected in test_cases:
        result = solution_func(nums[:], target)
        if sorted(result) == sorted(expected):
            passed += 1
            print(f"PASS | nums={nums}, target={target} -> {result}")
        else:
            print(
                f"FAIL | nums={nums}, target={target} -> got {result}, "
                f"expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(two_sum_sol1)
    run_basic_tests(two_sum_sol2)
    # run_basic_tests(two_sum_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
