"""
LeetCode 220 - Contains Duplicate III

Task:
Given an integer array `nums` and two integers `indexDiff` and `valueDiff`,
return `True` if there exist two indices `i` and `j` such that:

- `i != j`
- `abs(i - j) <= indexDiff`
- `abs(nums[i] - nums[j]) <= valueDiff`

Otherwise, return `False`.

Example 1:
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: True

Example 2:
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: False
"""

from sortedcontainers import SortedList

# Solution 1
def contains_nearby_almost_duplicate_sol1(
    nums: list[int], indexDiff: int, valueDiff: int
) -> bool:
    window = SortedList()
    
    # don't need left and right because size is strictly controlled by the indexDiff
    # therefore, use for loop instead of while for better control
    for i in range(len(nums)):
        pos = window.bisect_left(nums[i]) # check what this function does; doesn't actually insert, but gives u the position it shold be in in the list

        # check for the slightly larger number (determined through sortedList)
        # this makes sense because if adjacent sorted numbers aren't within valueDiff, nothing can
        # we do window[pos] so pos must < len(window), to make sure it has a larger number
        if pos < len(window) and window[pos] - nums[i] <= valueDiff:
            return True
        
        # now slightly smaller case
        # >0 to make sure it has a smaller number
        if pos > 0 and nums[i] - window[pos-1] <= valueDiff:
            return True
        
        # why check first then add? if add first, then the element might be comparing against itself in the window
        window.add(nums[i])

        # keeping sliding window approach: remove when it exceeds the window length
        if len(window) > indexDiff: 
            window.remove(nums[i-indexDiff])
    return False






# Solution 2
def contains_nearby_almost_duplicate_sol2(
    nums: list[int], indexDiff: int, valueDiff: int
) -> bool:
    # TODO: write your second solution
    raise NotImplementedError("Implement contains_nearby_almost_duplicate_sol2")


# Solution 3 (optional)
def contains_nearby_almost_duplicate_sol3(
    nums: list[int], indexDiff: int, valueDiff: int
) -> bool:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement contains_nearby_almost_duplicate_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 2, 3, 1], 3, 0, True),
        ([1, 5, 9, 1, 5, 9], 2, 3, False),
        ([1, 2], 0, 1, False),
        ([1, 0, 1, 1], 1, 2, True),
        ([-1, -1], 1, 0, True),
        ([1, 2, 3, 1], 1, 0, False),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, indexDiff, valueDiff, expected in test_cases:
        result = solution_func(nums[:], indexDiff, valueDiff)
        if result == expected:
            passed += 1
            print(
                f"PASS | nums={nums}, indexDiff={indexDiff}, "
                f"valueDiff={valueDiff} -> {result}"
            )
        else:
            print(
                f"FAIL | nums={nums}, indexDiff={indexDiff}, "
                f"valueDiff={valueDiff} -> got {result}, expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(contains_nearby_almost_duplicate_sol1)
    # run_basic_tests(contains_nearby_almost_duplicate_sol2)
    # run_basic_tests(contains_nearby_almost_duplicate_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
