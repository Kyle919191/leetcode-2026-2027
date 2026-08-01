"""
LeetCode 27 - Remove Element

Task:
Given an integer array `nums` and an integer `val`, remove all occurrences of
`val` in-place and return the number of elements not equal to `val` (`k`).

The relative order of elements may be changed. The first `k` elements of `nums`
should contain the elements not equal to `val`.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
"""


# Solution 1
def remove_element_sol1(nums: list[int], val: int) -> int:
    fast = slow = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1 
            #Notice a subtle difference from the sorted array deduplication solution: here we assign to nums[slow] first, then increment slow++. 
            # This ensures nums[0..slow-1] contains no elements equal to val, while the other solution guarantees that nums[0..slow] contains only unique elements
            # so the final result length is slow not slow+1
        fast += 1   
    return slow

# Solution 2
def remove_element_sol2(nums: list[int], val: int) -> int:
    raise NotImplementedError("Implement remove_element_sol2")


# Solution 3 (optional)
def remove_element_sol3(nums: list[int], val: int) -> int:
    raise NotImplementedError("Implement remove_element_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
        ([1, 2, 3], 4, 3, [1, 2, 3]),
        ([5, 5, 5], 5, 0, []),
        ([], 0, 0, []),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, val, expected_k, expected_values in test_cases:
        arr = nums[:]
        k = solution_func(arr, val)
        got_values = arr[:k]
        if k == expected_k and sorted(got_values) == sorted(expected_values):
            passed += 1
            print(f"PASS | nums={nums}, val={val} -> k={k}, first_k={got_values}")
        else:
            print(
                f"FAIL | nums={nums}, val={val} -> got k={k}, first_k={got_values}, "
                f"expected k={expected_k}, values={expected_values}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(remove_element_sol1)
    # run_basic_tests(remove_element_sol2)
    # run_basic_tests(remove_element_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
