"""
LeetCode 128 - Longest Consecutive Sequence
"""


def longest_consecutive_sol1(nums: list[int]) -> int:
    raise NotImplementedError("Implement longest_consecutive_sol1")


def longest_consecutive_sol2(nums: list[int]) -> int:
    raise NotImplementedError("Implement longest_consecutive_sol2")


def longest_consecutive_sol3(nums: list[int]) -> int:
    raise NotImplementedError("Implement longest_consecutive_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1], 1),
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
    # run_basic_tests(longest_consecutive_sol1)
    # run_basic_tests(longest_consecutive_sol2)
    # run_basic_tests(longest_consecutive_sol3)
    pass
