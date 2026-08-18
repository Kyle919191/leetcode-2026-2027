"""
LeetCode 153 - Find Minimum in Rotated Sorted Array
"""


def find_min_sol1(nums: list[int]) -> int:
    raise NotImplementedError("Implement find_min_sol1")


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
    # run_basic_tests(find_min_sol1)
    # run_basic_tests(find_min_sol2)
    # run_basic_tests(find_min_sol3)
    pass
