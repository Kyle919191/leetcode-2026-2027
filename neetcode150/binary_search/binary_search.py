"""
LeetCode 704 - Binary Search
"""


def binary_search_sol1(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1 # inclusive approach: both left and right are in consideration
    while left <= right: # when left == right, still one element to check(take [5] case)
        mid = left + (right-left) // 2 # prevent overflow for (left+right)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1 # since we use inclusive approach and we know mid is not index for target.
            # we can proceed to mid + 1 instead of mid
        else:
            right = mid - 1
    return -1



def binary_search_sol2(nums: list[int], target: int) -> int:
    raise NotImplementedError("Implement binary_search_sol2")


def binary_search_sol3(nums: list[int], target: int) -> int:
    raise NotImplementedError("Implement binary_search_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for nums, target, expected in test_cases:
        got = solution_func(nums[:], target)
        if got == expected:
            passed += 1
            print(f"PASS | nums={nums}, target={target} -> {got}")
        else:
            print(f"FAIL | nums={nums}, target={target} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(binary_search_sol1)
    # run_basic_tests(binary_search_sol2)
    # run_basic_tests(binary_search_sol3)
    pass
