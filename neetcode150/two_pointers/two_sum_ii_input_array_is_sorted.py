"""
LeetCode 167 - Two Sum II - Input Array Is Sorted
"""


def two_sum_ii_sol1(numbers: list[int], target: int) -> list[int]:
    # TODO-TALK: The array is sorted, so I can use two pointers from both ends.
    # TODO-TALK: If the sum is too small, I move left to increase it.
    # TODO-TALK: If the sum is too large, I move right to decrease it.
    left = 0 #index
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left+1, right+1]  # the index required by the problem starts from 1
        if sum < target:
            left += 1 # cannot move right pointer right because right is already at maximum
        elif sum > target:
            right -= 1
    return [-1, -1]


# Solution 2


def two_sum_ii_sol2(numbers: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement two_sum_ii_sol2")


def two_sum_ii_sol3(numbers: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement two_sum_ii_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for nums, target, expected in test_cases:
        got = solution_func(nums[:], target)
        if got == expected:
            passed += 1
            print(f"PASS | numbers={nums}, target={target} -> {got}")
        else:
            print(f"FAIL | numbers={nums}, target={target} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(two_sum_ii_sol1)
    # run_basic_tests(two_sum_ii_sol2)
    # run_basic_tests(two_sum_ii_sol3)
    pass
