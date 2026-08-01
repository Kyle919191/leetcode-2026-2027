"""
LeetCode 26 - Remove Duplicates from Sorted Array

Task:
Given an integer array `nums` sorted in non-decreasing order, remove duplicates
in-place so each unique element appears once. Return the number of unique
elements `k`.

The first `k` positions of `nums` should hold the unique elements.

Example 1:
Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""


# Solution 1
def remove_duplicates_sol1(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    slow = fast = 0
    
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow+1 #array length is index + 1, count first element


# Solution 2
def remove_duplicates_sol2(nums: list[int]) -> int:
    raise NotImplementedError("Implement remove_duplicates_sol2")


# Solution 3 (optional)
def remove_duplicates_sol3(nums: list[int]) -> int:
    raise NotImplementedError("Implement remove_duplicates_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([7, 7, 7, 7], 1, [7]),
        ([], 0, []),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, expected_k, expected_prefix in test_cases:
        arr = nums[:]
        k = solution_func(arr)
        got_prefix = arr[:k]
        if k == expected_k and got_prefix == expected_prefix:
            passed += 1
            print(f"PASS | nums={nums} -> k={k}, prefix={got_prefix}")
        else:
            print(
                f"FAIL | nums={nums} -> got k={k}, prefix={got_prefix}, "
                f"expected k={expected_k}, prefix={expected_prefix}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(remove_duplicates_sol1)
    # run_basic_tests(remove_duplicates_sol2)
    # run_basic_tests(remove_duplicates_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
