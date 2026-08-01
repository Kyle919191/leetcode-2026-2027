"""
LeetCode 287 - Find the Duplicate Number

Task:
Given an array of integers `nums` containing `n + 1` integers where each
integer is in the range `[1, n]` inclusive, there is only one repeated number.

Return this repeated number.

You must solve the problem without modifying the array and using only constant
extra space.

Example 1:
Input: nums = [1, 3, 4, 2, 2]
Output: 2

Example 2:
Input: nums = [3, 1, 3, 4, 2]
Output: 3
"""


# Solution 1

# treat the array index i as the node's val, and treat nums[i] as the next pointer, pointing to the node whose value is nums[i]
# each integer is in the range [1, n] guanrantees that every element we have is also a valid index
# duplicate guanrantees that there will be two elements that point to the same "node" "index"
# therefore, we can use the find cycle entry algorithm
# for example, nums = [1, 3, 4, 2, 2] is really ListNode(0) -> ListNode(1) -> ListNode(3) -> ListNode(2) -> ListNode(4)  -> ListNode(2)
def find_duplicate_sol1(nums: list[int]) -> int:
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
    # TODO: write your second solution
    raise NotImplementedError("Implement find_duplicate_sol2")


# Solution 3 (optional)
def find_duplicate_sol3(nums: list[int]) -> int:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement find_duplicate_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 1, 2], 1),
        ([2, 2, 2, 2, 2], 2),
        ([1, 4, 6, 3, 2, 5, 6], 6),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, expected in test_cases:
        result = solution_func(nums[:])
        if result == expected:
            passed += 1
            print(f"PASS | nums={nums} -> {result}")
        else:
            print(f"FAIL | nums={nums} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(find_duplicate_sol1)
    # run_basic_tests(find_duplicate_sol2)
    # run_basic_tests(find_duplicate_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
