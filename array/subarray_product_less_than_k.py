"""
LeetCode 713 - Subarray Product Less Than K

Task:
Given an array of integers `nums` and an integer `k`, return the number of
contiguous subarrays where the product of all the elements in the subarray is
strictly less than `k`.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0
"""


# Solution 1
def num_subarray_product_less_than_k_sol1(nums: list[int], k: int) -> int:
    count = 0
    left = right = 0
    product = 1

    while right < len(nums):
        product *= nums[right]
        right += 1

        if product > k and left < right:
            product //= nums[left]
            left += 1
        
        # how do we find the number of sub-arrays for a window a to b?
        # note that we're doing this sort of recursively. say our window is [1, 2]. now we add a new element 3 and it's still valid.
        # then, in our window [1, 2, 3], we don't actually want to count [1] [2] [1, 2] because they're counted in the last iteration.
        # instead, we only want to count subarrays that include the newest element we just added, 3. Therefore, we can use this rule:
        # for array of length n, the number of subarrays that contain the last element of the array (n-1th element) is n, which is right-left here
        count += right - left


# Solution 2
def num_subarray_product_less_than_k_sol2(nums: list[int], k: int) -> int:
    # TODO: write your second solution
    raise NotImplementedError("Implement num_subarray_product_less_than_k_sol2")


# Solution 3 (optional)
def num_subarray_product_less_than_k_sol3(nums: list[int], k: int) -> int:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement num_subarray_product_less_than_k_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([10, 5, 2, 6], 100, 8),
        ([1, 2, 3], 0, 0),
        ([1, 1, 1], 2, 6),
        ([1, 2, 3], 7, 6),
        ([100], 100, 0),
        ([100], 101, 1),
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
    # run_basic_tests(num_subarray_product_less_than_k_sol1)
    # run_basic_tests(num_subarray_product_less_than_k_sol2)
    # run_basic_tests(num_subarray_product_less_than_k_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
