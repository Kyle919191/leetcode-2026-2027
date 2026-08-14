"""
LeetCode 1004 - Max Consecutive Ones III

Task:
Given a binary array `nums` and an integer `k`, return the maximum number of
consecutive `1`s in the array if you can flip at most `k` zeros.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

Example 2:
Input: nums = [0,0,1,1,1,0,0], k = 0
Output: 3
"""


# Solution 1
def longest_ones_sol1(nums: list[int], k: int) -> int:
    left = right = 0
    max_len = -1
    one_count = 0

    while right < len(nums):
        if nums[right] == 1:
            one_count += 1
        right += 1

        while (right - left - one_count) > k:
            if nums[left] == 1:
                one_count -= 1
            left += 1
        
        # now we have a valid window: calculate length
        max_len = max(max_len, right - left)
    return max_len


# Solution 2
def longest_ones_sol2(nums: list[int], k: int) -> int:
    # TODO: write your second solution
    raise NotImplementedError("Implement longest_ones_sol2")


# Solution 3 (optional)
def longest_ones_sol3(nums: list[int], k: int) -> int:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement longest_ones_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 1, 0, 0], 0, 3),
        ([0, 0, 0], 1, 1),
        ([1, 1, 1], 2, 3),
        ([0], 1, 1),
        ([0], 0, 0),
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
    run_basic_tests(longest_ones_sol1)
    # run_basic_tests(longest_ones_sol2)
    # run_basic_tests(longest_ones_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
