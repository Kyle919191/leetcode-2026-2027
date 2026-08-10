"""
LeetCode 704 - Binary Search

Task:
Given an array of integers `nums` sorted in ascending order, and an integer
`target`, write a function to search `target` in `nums`.

If `target` exists, return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
"""


# Solution 1
def binary_search_sol1(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    # We use closed interval [left, right].
    # right starts at len(nums) - 1 because right is included in the search space.
    # (If we used right = len(nums), that would be left-closed-right-open [left, right).)

    # Must use left <= right for closed interval.
    # When left == right, one candidate index is still left to check.
    # If we used left < right, we'd skip that last element.
    while left <= right:
        mid = left + (right - left) // 2 # instead of (right+left)//2 to prevent overflow
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


# Closed-interval binary search templates [left, right].
def binary_search(nums: list[int], target: int) -> int:
    # set left and right indexes
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # found the target value
            return mid
    # target value not found
    return -1


def left_bound(nums: list[int], target: int) -> int:
    # set left and right indexes
    left, right = 0, len(nums) - 1
    # We are searching on closed interval [left, right].
    # On nums[mid] == target, we DO NOT return immediately.
    # Instead, we keep shrinking to the left side (right = mid - 1)
    # to see if there is an earlier target occurrence.
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            # target exists, narrow the right boundary
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    # Key difference vs regular binary_search:
    # - regular binary_search asks: "does target exist?" so it can return mid immediately on ==.
    # - left_bound asks: "what is the leftmost target index?" so == is not final;
    #   we must keep searching left side until left > right to prove optimality.
    #
    # Why can this work even if a loop iteration does not explicitly check nums[left]?
    # Because once left > right, the search interval is empty, and left is exactly
    # the first position where target could appear (lower_bound position).
    #
    # Case A: nums = [5, 7, 7, 8, 8, 10], target = 8
    # Iter1: left=0,right=5,mid=2 -> nums[mid]=7 < 8  => left=3
    # Iter2: left=3,right=5,mid=4 -> nums[mid]=8 == 8 => right=3
    # Iter3: left=3,right=3,mid=3 -> nums[mid]=8 == 8 => right=2
    # Stop: left=3,right=2 (left > right), answer is left=3.
    #
    # Case B: nums = [5, 7, 7, 7, 8, 10], target = 8
    # Iter1: left=0,right=5,mid=2 -> nums[mid]=7 < 8  => left=3
    # Iter2: left=3,right=5,mid=4 -> nums[mid]=8 == 8 => right=3
    # Iter3: left=3,right=3,mid=3 -> nums[mid]=7 < 8  => left=4
    # Stop: left=4,right=3 (left > right), answer is left=4.
    #
    # In Case B, we did not "check nums[left]" at the stop moment.
    # That is fine: iter3 proved index 3 is too small, so boundary must be to its right.
    # The final validation below confirms whether target actually exists at that boundary.
    # determine if the target exists
    if left < 0 or left >= len(nums):
        return -1
    # determine if the left boundary found is the target value
    return left if nums[left] == target else -1


def right_bound(nums: list[int], target: int) -> int:
    # set left and right indexes
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            # target exists, narrow the left boundary
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # Symmetric idea of left_bound:
    # right_bound also cannot return immediately on ==, because it needs the
    # rightmost target index. It keeps searching right until left > right.
    # determine if the target exists
    if right < 0 or right >= len(nums):
        return -1
    # determine if the right boundary found is the target value
    return right if nums[right] == target else -1


# Solution 2
def binary_search_sol2(nums: list[int], target: int) -> int:
    return binary_search(nums, target)


# Solution 3 (optional)
def binary_search_sol3(nums: list[int], target: int) -> int:
    raise NotImplementedError("Implement binary_search_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
        ([1, 2, 3, 4, 5, 6, 7], 1, 0),
        ([1, 2, 3, 4, 5, 6, 7], 7, 6),
        ([1, 2, 3, 4, 5, 6, 7], 4, 3),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, target, expected in test_cases:
        result = solution_func(nums[:], target)
        if result == expected:
            passed += 1
            print(f"PASS | nums={nums}, target={target} -> {result}")
        else:
            print(
                f"FAIL | nums={nums}, target={target} -> got {result}, "
                f"expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(binary_search_sol1)
    # run_basic_tests(binary_search_sol2)
    # run_basic_tests(binary_search_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
