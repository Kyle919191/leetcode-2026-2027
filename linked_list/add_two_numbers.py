"""
LeetCode 2 - Add Two Numbers

Task:
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each node contains a
single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example 1:
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def add_two_numbers_sol1(
    l1: ListNode | None,
    l2: ListNode | None,
) -> ListNode | None:
    dummy = ListNode(-1)
    p = dummy
    p1, p2 = l1, l2
    carry = 0

    while p1 is not None or p2 is not None or carry > 0: # carry>0 case say last digit for p1+p2>10, need trailing number
        val = carry
        if p1 is not None: # p1 and p2 can be different length
            val += p1.val
            p1 = p1.next
        if p2 is not None:
            val += p2.val
            p2 = p2.next
        single_digit_val = val % 10 #keep val as single digit, 
        #use another variable so original var is kept, allowing next line to work properly
        carry = val // 10

        p.next = ListNode(single_digit_val)
        p = p.next
    return dummy.next


# Solution 2
def add_two_numbers_sol2(
    l1: ListNode | None,
    l2: ListNode | None,
) -> ListNode | None:
    # TODO: write your second solution
    raise NotImplementedError("Implement add_two_numbers_sol2")


# Solution 3 (optional)
def add_two_numbers_sol3(
    l1: ListNode | None,
    l2: ListNode | None,
) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement add_two_numbers_sol3")


def build_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    cur = dummy
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    out: list[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1, 8], [0], [1, 8]),
        ([5], [5], [0, 1]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for l1_vals, l2_vals, expected in test_cases:
        l1 = build_linked_list(l1_vals)
        l2 = build_linked_list(l2_vals)
        result_head = solution_func(l1, l2)
        result = linked_list_to_list(result_head)
        if result == expected:
            passed += 1
            print(f"PASS | l1={l1_vals}, l2={l2_vals} -> {result}")
        else:
            print(
                f"FAIL | l1={l1_vals}, l2={l2_vals} -> "
                f"got {result}, expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(add_two_numbers_sol1)
    # run_basic_tests(add_two_numbers_sol2)
    # run_basic_tests(add_two_numbers_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
