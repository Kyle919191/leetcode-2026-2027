"""
LeetCode 239 - Sliding Window Maximum
"""


def max_sliding_window_sol1(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError("Implement max_sliding_window_sol1")


def max_sliding_window_sol2(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError("Implement max_sliding_window_sol2")


def max_sliding_window_sol3(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError("Implement max_sliding_window_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([9, 11], 2, [11]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for nums, k, expected in test_cases:
        got = solution_func(nums[:], k)
        if got == expected:
            passed += 1
            print(f"PASS | nums={nums}, k={k} -> {got}")
        else:
            print(f"FAIL | nums={nums}, k={k} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(max_sliding_window_sol1)
    # run_basic_tests(max_sliding_window_sol2)
    # run_basic_tests(max_sliding_window_sol3)
    pass
