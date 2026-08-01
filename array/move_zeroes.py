"""
LeetCode 283 - Move Zeroes

Task:
Given an integer array `nums`, move all zeroes to the end while keeping the
relative order of non-zero elements.

Do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

from remove_element import remove_element_sol1


# Solution 1
def move_zeroes_sol1(nums: list[int]) -> None:
    p = remove_element_sol1(nums, 0) # p = # of remaining elements. so pth index doesn't have a remaining element

    for i in range(p, len(nums)):
        nums[i] = 0


# Solution 2
def move_zeroes_sol2(nums: list[int]) -> None:
    raise NotImplementedError("Implement move_zeroes_sol2")


# Solution 3 (optional)
def move_zeroes_sol3(nums: list[int]) -> None:
    raise NotImplementedError("Implement move_zeroes_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 0], [0, 0, 0]),
        ([4, 0, 5, 0, 0, 3, 0, 1], [4, 5, 3, 1, 0, 0, 0, 0]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, expected in test_cases:
        arr = nums[:]
        solution_func(arr)
        if arr == expected:
            passed += 1
            print(f"PASS | nums={nums} -> {arr}")
        else:
            print(f"FAIL | nums={nums} -> got {arr}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(move_zeroes_sol1)
    # run_basic_tests(move_zeroes_sol2)
    # run_basic_tests(move_zeroes_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
