"""
LeetCode 92 - Reverse Linked List II

Task:
Given the head of a singly linked list and two integers `left` and `right`
where `left <= right`, reverse the nodes from position `left` to position
`right`, and return the reversed list.

Example 1:
Input: head = [1, 2, 3, 4, 5], left = 2, right = 4
Output: [1, 4, 3, 2, 5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""

from reverse_first_n_nodes_of_linked_list import (
    reverse_first_n_sol1,
    reverse_first_n_sol2,
)


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def reverse_between_sol1(
    head: ListNode | None,
    left: int,
    right: int,
) -> ListNode | None:
    if head is None or left == right:
        return head

    if left == 1:
        return reverse_first_n_sol1(head, right)

    pre = head
    for _ in range(1, left - 1):  # go to the node right before the left-th node
        if pre is None:
            return head
        pre = pre.next

    if pre is None or pre.next is None:
        return head

    # say left=2, right=4; we want to reverse 3 nodes starting at 2,
    # so count = right - left + 1 = 4 - 2 + 1 = 3
    pre.next = reverse_first_n_sol1(pre.next, right - left + 1)
    # the helper will return the head of the reversed list,
    # so we should do pre.next = reverse...
    # the helper reverse... takes care of how the original head/new tail
    # links to the remaining parts of the original list, so we're good
    return head


# Solution 2
def reverse_between_sol2(
    head: ListNode | None,
    left: int,
    right: int,
) -> ListNode | None:
    if head is None or left == right:
        return head
    if left == 1:
        return reverse_first_n_sol2(head, right)
    
    head.next = reverse_between_sol2(head.next, left - 1, right - 1)
    return head



# Solution 3 (optional)
def reverse_between_sol3(
    head: ListNode | None,
    left: int,
    right: int,
) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement reverse_between_sol3")


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
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
        ([1, 2], 1, 2, [2, 1]),
        ([1, 2, 3], 1, 1, [1, 2, 3]),
        ([1, 2, 3, 4], 3, 4, [1, 2, 4, 3]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, left, right, expected in test_cases:
        head = build_linked_list(values)
        result_head = solution_func(head, left, right)
        result = linked_list_to_list(result_head)
        if result == expected:
            passed += 1
            print(
                f"PASS | head={values}, left={left}, right={right} -> {result}"
            )
        else:
            print(
                f"FAIL | head={values}, left={left}, right={right} -> "
                f"got {result}, expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    #run_basic_tests(reverse_between_sol1)
    run_basic_tests(reverse_between_sol2)
    # run_basic_tests(reverse_between_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
