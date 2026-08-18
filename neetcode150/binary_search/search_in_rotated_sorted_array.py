"""
LeetCode 33 - Search in Rotated Sorted Array
"""


def search_sol1(nums: list[int], target: int) -> int:
    raise NotImplementedError("Implement search_sol1")


def search_sol2(nums: list[int], target: int) -> int:
    raise NotImplementedError("Implement search_sol2")


def search_sol3(nums: list[int], target: int) -> int:
    raise NotImplementedError("Implement search_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
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
    # run_basic_tests(search_sol1)
    # run_basic_tests(search_sol2)
    # run_basic_tests(search_sol3)
    pass
