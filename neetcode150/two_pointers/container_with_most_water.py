"""
LeetCode 11 - Container With Most Water
"""


def max_area_sol1(height: list[int]) -> int:
    raise NotImplementedError("Implement max_area_sol1")


def max_area_sol2(height: list[int]) -> int:
    raise NotImplementedError("Implement max_area_sol2")


def max_area_sol3(height: list[int]) -> int:
    raise NotImplementedError("Implement max_area_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for height, expected in test_cases:
        got = solution_func(height[:])
        if got == expected:
            passed += 1
            print(f"PASS | height={height} -> {got}")
        else:
            print(f"FAIL | height={height} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(max_area_sol1)
    # run_basic_tests(max_area_sol2)
    # run_basic_tests(max_area_sol3)
    pass
