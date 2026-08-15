"""
LeetCode 238 - Product of Array Except Self
"""


def product_except_self_sol1(nums: list[int]) -> list[int]:
    raise NotImplementedError("Implement product_except_self_sol1")


def product_except_self_sol2(nums: list[int]) -> list[int]:
    raise NotImplementedError("Implement product_except_self_sol2")


def product_except_self_sol3(nums: list[int]) -> list[int]:
    raise NotImplementedError("Implement product_except_self_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
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
    # run_basic_tests(product_except_self_sol1)
    # run_basic_tests(product_except_self_sol2)
    # run_basic_tests(product_except_self_sol3)
    pass
