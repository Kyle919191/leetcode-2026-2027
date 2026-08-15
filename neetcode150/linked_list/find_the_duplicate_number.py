"""
LeetCode 287 - Find the Duplicate Number
"""


def find_duplicate_sol1(nums: list[int]) -> int:
    # TODO-TALK: I treat values as next pointers and run Floyd cycle detection.
    # TODO-TALK: First phase finds an intersection point inside the cycle.
    # TODO-TALK: Second phase resets one pointer to start; where they meet again is the duplicate.
    fast = slow = 0
    while True:
        fast = nums[nums[fast]] # equivalent to
        slow = nums[slow]
        if slow == fast:
            break
    # cannot do:
    # while slow != fast:
    #    fast = nums[nums[fast]] # equivalent to
    #    slow = nums[slow]
    # because fast and slow start with the same value
    # do this as alternative:
    # slow = nums[0]
    # fast = nums[nums[0]]
    # while slow != fast:
    #     slow = nums[slow]
    #     fast = nums[nums[fast]]

    slow = 0 #rewind slow back to head
    while slow != fast:
        fast = nums[fast]
        slow = nums[slow]
    return slow

# Solution 2


def find_duplicate_sol2(nums: list[int]) -> int:
    raise NotImplementedError("Implement find_duplicate_sol2")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 1, 2], 1),
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
    # run_basic_tests(find_duplicate_sol1)
    # run_basic_tests(find_duplicate_sol2)
    pass
