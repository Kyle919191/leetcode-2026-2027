"""
LeetCode 875 - Koko Eating Bananas
"""


def min_eating_speed_sol1(piles: list[int], h: int) -> int:
    raise NotImplementedError("Implement min_eating_speed_sol1")


def min_eating_speed_sol2(piles: list[int], h: int) -> int:
    raise NotImplementedError("Implement min_eating_speed_sol2")


def min_eating_speed_sol3(piles: list[int], h: int) -> int:
    raise NotImplementedError("Implement min_eating_speed_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for piles, h, expected in test_cases:
        got = solution_func(piles[:], h)
        if got == expected:
            passed += 1
            print(f"PASS | piles={piles}, h={h} -> {got}")
        else:
            print(f"FAIL | piles={piles}, h={h} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(min_eating_speed_sol1)
    # run_basic_tests(min_eating_speed_sol2)
    # run_basic_tests(min_eating_speed_sol3)
    pass
