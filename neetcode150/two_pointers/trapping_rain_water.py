"""
LeetCode 42 - Trapping Rain Water
"""


def trap_sol1(height: list[int]) -> int:
    raise NotImplementedError("Implement trap_sol1")


def trap_sol2(height: list[int]) -> int:
    raise NotImplementedError("Implement trap_sol2")


def trap_sol3(height: list[int]) -> int:
    raise NotImplementedError("Implement trap_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0),
        ([1, 2, 3], 0),
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
    # run_basic_tests(trap_sol1)
    # run_basic_tests(trap_sol2)
    # run_basic_tests(trap_sol3)
    pass
