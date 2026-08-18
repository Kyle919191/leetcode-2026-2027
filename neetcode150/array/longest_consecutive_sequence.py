"""
LeetCode 128 - Longest Consecutive Sequence
"""


def longest_consecutive_sol1(nums: list[int]) -> int:
    num_set = set(nums)
    max_len = 0
    for num in nums:
        # TODO-TALK: Only start counting from sequence starts.
        if num-1 in num_set: # if num is not the start of a consecutive list, dont count it
            continue
        length = 0
        cur = num
        # TODO-TALK: Expand forward while consecutive values exist.
        while cur in num_set:
            cur+=1
            length+=1
        max_len = max(max_len, length)
    return max_len


def longest_consecutive_sol2(nums: list[int]) -> int:
    raise NotImplementedError("Implement longest_consecutive_sol2")


def longest_consecutive_sol3(nums: list[int]) -> int:
    raise NotImplementedError("Implement longest_consecutive_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1], 1),
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
    run_basic_tests(longest_consecutive_sol1)
    # run_basic_tests(longest_consecutive_sol2)

