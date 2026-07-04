"""
LeetCode 21 - Merge Two Sorted Lists

Task:
You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one sorted linked list and return its head.

Example 1:
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]

Example 2:
Input: list1 = [], list2 = []
Output: []
"""


from logging import NullHandler


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def merge_two_lists_sol1(
    list1: ListNode | None,
    list2: ListNode | None,
) -> ListNode | None: 

    dummy = ListNode(-1)
    p = dummy

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            p.next = list1
            list1 = list1.next
        else:
            p.next = list2
            list2 = list2.next
        p = p.next
        p.next = None
    if list1 is None:
        p.next = list2
    if list2 is None:
        p.next = list1
    return dummy.next

# Solution 2
def merge_two_lists_sol2(
    list1: ListNode | None,
    list2: ListNode | None,
) -> ListNode | None:
    # TODO: write your second solution
    raise NotImplementedError("Implement merge_two_lists_sol2")


# Solution 3 (optional)
def merge_two_lists_sol3(
    list1: ListNode | None,
    list2: ListNode | None,
) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement merge_two_lists_sol3")


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
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([0], [], [0]),
        ([1, 5], [2, 3, 4], [1, 2, 3, 4, 5]),
        ([1, 1, 2], [1, 3], [1, 1, 1, 2, 3]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for list1_vals, list2_vals, expected in test_cases:
        list1 = build_linked_list(list1_vals)
        list2 = build_linked_list(list2_vals)
        result_head = solution_func(list1, list2)
        result = linked_list_to_list(result_head)
        if result == expected:
            passed += 1
            print(
                f"PASS | list1={list1_vals}, list2={list2_vals} -> {result}"
            )
        else:
            print(
                f"FAIL | list1={list1_vals}, list2={list2_vals} -> "
                f"got {result}, expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(merge_two_lists_sol1)
    # run_basic_tests(merge_two_lists_sol2)
    # run_basic_tests(merge_two_lists_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
