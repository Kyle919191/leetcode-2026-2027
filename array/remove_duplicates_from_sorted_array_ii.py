"""
LeetCode 80 - Remove Duplicates from Sorted Array II

Task:
Given an integer array `nums` sorted in non-decreasing order, remove some
duplicates in-place such that each unique element appears at most twice.

The relative order of the elements should be kept the same.

Return `k` after placing the final result in the first `k` positions of `nums`.

Do not allocate extra space for another array. You must do this by modifying
the input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
"""


# Solution 1
def remove_duplicates_ii_sol1(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    slow = fast = 0
    count = 0
    while fast < len(nums):
        if nums[slow] != nums[fast]: # new unique element
            slow += 1
            nums[slow] = nums[fast]
            count = 0 # since new element, set to 0. later will +=1, meaning we've seen this element once
        elif slow < fast and count < 2:
            slow += 1
            nums[slow] = nums[fast]
        
        # both cases need count +=1
        fast += 1
        count += 1
    return slow + 1


# Solution 2
def remove_duplicates_ii_sol2(nums: list[int]) -> int:
    # TODO: write your second solution
    raise NotImplementedError("Implement remove_duplicates_ii_sol2")


# Solution 3 (optional)
def remove_duplicates_ii_sol3(nums: list[int]) -> int:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement remove_duplicates_ii_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
        ([1, 1, 1, 1], 2, [1, 1]),
        ([1, 2, 3], 3, [1, 2, 3]),
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
    run_basic_tests(remove_duplicates_ii_sol1)
    # run_basic_tests(remove_duplicates_ii_sol2)
    # run_basic_tests(remove_duplicates_ii_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
