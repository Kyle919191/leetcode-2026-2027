"""
LeetCode 153 - Find Minimum in Rotated Sorted Array
"""


def find_min_sol1(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    ans = nums[0]
    while left <= right:
        mid = left + (right - left) // 2
        ans = min(ans, nums[mid]) # again, early record mid before we exlcude mid away in if and elif
        if nums[mid] > nums[right]: # exploit the fact that this list is still locally sorted
            # A rotated sorted array has exactly one “drop” point, so if nums[mid] < nums[right], 
            # then [mid, right] is fully sorted and cannot contain a smaller value than nums[mid]. 
            # Therefore, the minimum must be at mid or somewhere to its left, so we safely do right = mid
            # it is not possible that at some point, say nums[right]>nums[mid], but the minimum exists between right and mid
            # TODO-TALK: Compare mid with right to decide which half contains min.
            left = mid + 1
        else:
            right = mid - 1
    return ans


def find_min_sol2(nums: list[int]) -> int:
    raise NotImplementedError("Implement find_min_sol2")


def find_min_sol3(nums: list[int]) -> int:
    raise NotImplementedError("Implement find_min_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for nums, expected in test_cases:
        got = solution_func(nums[:])
        if got == expected:
            passed += 1
            print(f"PASS | nums={nums} -> {got}")
        else:
            print(f"FAIL | nums={nums} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(find_min_sol1)
    # run_basic_tests(find_min_sol2)
    # run_basic_tests(find_min_sol3)

