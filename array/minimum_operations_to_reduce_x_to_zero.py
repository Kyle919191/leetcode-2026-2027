"""
LeetCode 1658 - Minimum Operations to Reduce X to Zero

Task:
You are given an integer array `nums` and an integer `x`.

In one operation, you can either remove the leftmost or the rightmost element
from the array and subtract its value from `x`.

Return the minimum number of operations to reduce `x` to exactly `0` if it is
possible, otherwise return `-1`.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
"""


# Solution 1
# similar problem but with negative integers: 560. Subarray Sum Equals K (have to use prefix sum)
# for this problem, rephrase: we want to find the longest sub-array such that their sum=sum(nums)-x
# for example 1, we want to find the array 114, which sums to 6, which is 11-5
# we can use sliding window in this case due to an important phrase in the question: in one operation we can either
# remove the leftmost or rightmost only, not just any element. This means the array we're left with have to be continuous(an subarray)
def min_operations_sol1(nums: list[int], x: int) -> int:
    n = len(nums)
    left = right = 0
    max_len = -1
    window_sum = 0
    target = sum(nums) - x
    if target < 0:
        return -1
    if target == 0:
        return n

    while right < n:
        window_sum += nums[right]
        right +=1

        while window_sum > target and left < right: # other sliding window questions do this implicitly...check. for example, anagram question had smth like window_size >= len(p)
            window_sum -= nums[left]
            left += 1
        
        if window_sum == target:
            max_len = max(max_len, right - left) # we don't return right away! there can be multiple valid choices and we want to find longest subarray

    return -1 if max_len == -1 else n - max_len



# Solution 2
def min_operations_sol2(nums: list[int], x: int) -> int:
    # TODO: write your second solution
    raise NotImplementedError("Implement min_operations_sol2")


# Solution 3 (optional)
def min_operations_sol3(nums: list[int], x: int) -> int:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement min_operations_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 1, 4, 2, 3], 5, 2),
        ([5, 6, 7, 8, 9], 4, -1),
        ([3, 2, 20, 1, 1, 3], 10, 5),
        ([1, 1], 3, -1),
        ([1, 1], 2, 2),
        ([1], 1, 1),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, x, expected in test_cases:
        result = solution_func(nums[:], x)
        if result == expected:
            passed += 1
            print(f"PASS | nums={nums}, x={x} -> {result}")
        else:
            print(f"FAIL | nums={nums}, x={x} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(min_operations_sol1)
    # run_basic_tests(min_operations_sol2)
    # run_basic_tests(min_operations_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
