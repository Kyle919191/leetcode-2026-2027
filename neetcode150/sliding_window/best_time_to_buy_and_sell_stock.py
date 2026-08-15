"""
LeetCode 121 - Best Time to Buy and Sell Stock
"""


def max_profit_sol1(prices: list[int]) -> int:
    raise NotImplementedError("Implement max_profit_sol1")


def max_profit_sol2(prices: list[int]) -> int:
    raise NotImplementedError("Implement max_profit_sol2")


def max_profit_sol3(prices: list[int]) -> int:
    raise NotImplementedError("Implement max_profit_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for prices, expected in test_cases:
        got = solution_func(prices[:])
        if got == expected:
            passed += 1
            print(f"PASS | prices={prices} -> {got}")
        else:
            print(f"FAIL | prices={prices} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(max_profit_sol1)
    # run_basic_tests(max_profit_sol2)
    # run_basic_tests(max_profit_sol3)
    pass
