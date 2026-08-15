"""
LeetCode 1 - Two Sum
"""


def two_sum_sol1(nums: list[int], target: int) -> list[int]:
    # TODO-TALK: The brute force way checks every pair, but that is quadratic.
    # TODO-TALK: I want a linear pass, so I will keep a map of seen values and their indices.
    index_by_value = {}
    for i, x in enumerate(nums):
        # TODO-TALK: At each step, I treat the current number as the second number in the pair.
        # TODO-TALK: The first number must be target minus current value.
        need = target - x
        # TODO-TALK: If that needed value is already in the map, the answer is ready right now.
        # TODO-TALK: The earlier index comes from the map and the current index is i.
        if need in index_by_value:
            return [index_by_value[need], i]
        # TODO-TALK: If not found, I record the current value for future elements.
        index_by_value[x] = i
    # TODO-TALK: This return is just a fallback in case no valid pair exists.
    return []


# Solution 2


def two_sum_sol2(nums: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement two_sum_sol2")


def two_sum_sol3(nums: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement two_sum_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for nums, target, expected in test_cases:
        got = solution_func(nums[:], target)
        if sorted(got) == sorted(expected):
            passed += 1
            print(f"PASS | nums={nums}, target={target} -> {got}")
        else:
            print(f"FAIL | nums={nums}, target={target} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(two_sum_sol1)
    # run_basic_tests(two_sum_sol2)
    # run_basic_tests(two_sum_sol3)
    pass
