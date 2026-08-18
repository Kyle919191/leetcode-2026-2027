"""
LeetCode 739 - Daily Temperatures
"""


def daily_temperatures_sol1(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i, t in enumerate(temperatures):
        # TODO-TALK: While current day is warmer, resolve waiting colder days.
        # so at any moment, stack contains the days(index) that haven't been resolved, and when a new number comes in, 
        # we want to try to resolve everything in the stack. therefore, result[j] = i-j gets the difference between our current
        # day index vs the day index we just determined can be resolved
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            result[j] = i-j
        stack.append(i)
    return result



def daily_temperatures_sol2(temperatures: list[int]) -> list[int]:
    raise NotImplementedError("Implement daily_temperatures_sol2")


def daily_temperatures_sol3(temperatures: list[int]) -> list[int]:
    raise NotImplementedError("Implement daily_temperatures_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for temperatures, expected in test_cases:
        got = solution_func(temperatures[:])
        if got == expected:
            passed += 1
            print(f"PASS | temperatures={temperatures} -> {got}")
        else:
            print(f"FAIL | temperatures={temperatures} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(daily_temperatures_sol1)
    # run_basic_tests(daily_temperatures_sol2)
    # run_basic_tests(daily_temperatures_sol3)

