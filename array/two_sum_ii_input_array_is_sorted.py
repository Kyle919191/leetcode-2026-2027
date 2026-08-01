"""
LeetCode 167 - Two Sum II - Input Array Is Sorted

Task:
Given a 1-indexed array of integers `numbers` that is sorted in non-decreasing
order, find two numbers such that they add up to `target`.

Return the indices of the two numbers, added by one, as an integer array
`[index1, index2]` of length 2 where `1 <= index1 < index2 <= numbers.length`.

You may assume exactly one solution exists, and you may not use the same
element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
"""


# Solution 1
def two_sum_ii_sol1(numbers: list[int], target: int) -> list[int]:
# Whenever you see a sorted array, think two pointers. 
# The approach here is similar to binary search, by adjusting left and right, you can control the value of sum
# sorted is intuitive because: when we move a pointer to the left, sum always greater; vice versa
    left = 0 #index
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left+1, right+1]  # the index required by the problem starts from 1
        if sum < target:
            left += 1 # cannot move right pointer right because right is already at maximum
        elif sum > target:
            right -= 1
    return [-1, -1]


# Solution 2
def two_sum_ii_sol2(numbers: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement two_sum_ii_sol2")


# Solution 3 (optional)
def two_sum_ii_sol3(numbers: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement two_sum_ii_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9], 8, [4, 5]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for numbers, target, expected in test_cases:
        result = solution_func(numbers[:], target)
        if result == expected:
            passed += 1
            print(f"PASS | numbers={numbers}, target={target} -> {result}")
        else:
            print(
                f"FAIL | numbers={numbers}, target={target} -> got {result}, "
                f"expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(two_sum_ii_sol1)
    # run_basic_tests(two_sum_ii_sol2)
    # run_basic_tests(two_sum_ii_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
