"""
LeetCode 217 - Contains Duplicate
"""


def contains_duplicate_sol1(nums: list[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False



def contains_duplicate_sol2(nums: list[int]) -> bool:
    raise NotImplementedError("Implement contains_duplicate_sol2")


def contains_duplicate_sol3(nums: list[int]) -> bool:
    raise NotImplementedError("Implement contains_duplicate_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
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
    run_basic_tests(contains_duplicate_sol1)
    # run_basic_tests(contains_duplicate_sol2)
    # run_basic_tests(contains_duplicate_sol3)

