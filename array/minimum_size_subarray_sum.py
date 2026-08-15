"""
LeetCode 209 - Minimum Size Subarray Sum

Task:
Given an array of positive integers `nums` and a positive integer `target`,
return the minimal length of a contiguous subarray of which the sum is greater
than or equal to `target`.

If there is no such subarray, return `0` instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""


# Solution 1
def min_sub_array_len_sol1(target: int, nums: list[int]) -> int:
    left = right = 0
    sum = 0
    min_len = float('inf')

    while right < len(nums):
        sum += nums[right]
        right +=1

        while sum >= target and left < right:
            # entering this while loop means we've reached above the target, so it's valid
            min_len = min(min_len, right - left)
            sum -= nums[left]
            left += 1
    
    return 0 if min_len == float('inf') else min_len


# Solution 2
def min_sub_array_len_sol2(target: int, nums: list[int]) -> int:
    # TODO: write your second solution
    raise NotImplementedError("Implement min_sub_array_len_sol2")


# Solution 3 (optional)
def min_sub_array_len_sol3(target: int, nums: list[int]) -> int:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement min_sub_array_len_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (15, [1, 2, 3, 4, 5], 5),
        (100, [1, 2, 3], 0),
        (3, [1, 1, 1], 3),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for target, nums, expected in test_cases:
        result = solution_func(target, nums[:])
        if result == expected:
            passed += 1
            print(f"PASS | target={target}, nums={nums} -> {result}")
        else:
            print(
                f"FAIL | target={target}, nums={nums} -> "
                f"got {result}, expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(min_sub_array_len_sol1)
    # run_basic_tests(min_sub_array_len_sol2)
    # run_basic_tests(min_sub_array_len_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
