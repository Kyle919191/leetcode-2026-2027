"""
LeetCode 121 - Best Time to Buy and Sell Stock
"""


def max_profit_sol1(prices: list[int]) -> int:
    # reason why we keep track of min_price: if we decide to sell at day n, the most optimal solution
    # is to buy at the minimum-price day before n. However, keep in mind this doesn't guanrantee that
    # the most optimal purchase must happen at the global min_price. consider the example [7, 5, 100, 1, 3]:
    # best buy day is 5 best sell day is 100, although 5 is not the global min_price. However, this at least shows
    # that buying at 5 is better than buying at 7, because 5 is the min_price before 100.
    min_price = float('inf')
    best_profit = 0

    for p in prices:
        # TODO-TALK: Keep best buy price seen so far.
        min_price = min(min_price, p)
        # TODO-TALK: Treat today as sell day and update max profit.
        best_profit = max(best_profit, p-min_price)
    return best_profit


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
    run_basic_tests(max_profit_sol1)
    # run_basic_tests(max_profit_sol2)
    # run_basic_tests(max_profit_sol3)

