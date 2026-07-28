"""
LeetCode 234 - Palindrome Linked List

Task:
Given the head of a singly linked list, return `True` if it is a palindrome,
or `False` otherwise.

Example 1:
Input: head = [1, 2, 2, 1]
Output: True

Example 2:
Input: head = [1, 2]
Output: False
"""

from reverse_linked_list import (
    reverse_list_sol1
)


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def is_palindrome_sol1(head: ListNode | None) -> bool:
    slow= head
    fast = head
    left = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    if fast is not None:
        slow = slow.next # we want slow to be the first node of the right part
        # when list is even, it's naturally the case. when list is odd(determined by fast is not None)
        # we have to move slow one step forward

    right = reverse_list_sol1(slow)
    reversed_right_head = right
    is_palindrome = True

    while right is not None:
        if left.val != right.val:
            is_palindrome = False
            break
        left = left.next
        right = right.next

    # restore original list structure
    reverse_list_sol1(reversed_right_head)

    return is_palindrome


# Solution 2
def is_palindrome_sol2(head: ListNode | None) -> bool:
    # TODO: write your second solution
    raise NotImplementedError("Implement is_palindrome_sol2")


# Solution 3 (optional)
def is_palindrome_sol3(head: ListNode | None) -> bool:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement is_palindrome_sol3")


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
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 4, 1], False),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, expected in test_cases:
        head = build_linked_list(values)
        before = linked_list_to_list(head)
        result = solution_func(head)
        after = linked_list_to_list(head)
        restored = before == after

        print(
            f"LIST CHECK | before={before}, after={after}, restored={restored}"
        )

        if result == expected:
            passed += 1
            print(f"PASS | head={values} -> {result}")
        else:
            print(f"FAIL | head={values} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(is_palindrome_sol1)
    # run_basic_tests(is_palindrome_sol2)
    # run_basic_tests(is_palindrome_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
