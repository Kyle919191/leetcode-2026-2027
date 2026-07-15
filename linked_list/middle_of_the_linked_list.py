"""
LeetCode 876 - Middle of the Linked List

Task:
Given the head of a singly linked list, return the middle node.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1, 2, 3, 4, 5]
Output: [3, 4, 5]

Example 2:
Input: head = [1, 2, 3, 4, 5, 6]
Output: [4, 5, 6]
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def middle_node_sol1(head: ListNode | None) -> ListNode | None:
    if head is None:
        return None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


# Solution 2
def middle_node_sol2(head: ListNode | None) -> ListNode | None:
    if head is None:
        return None
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


# Solution 3 (optional)
def middle_node_sol3(head: ListNode | None) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement middle_node_sol3")


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
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
        ([1], [1]),
        ([1, 2], [2]),
        ([1, 2, 3, 4], [3, 4]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, expected in test_cases:
        head = build_linked_list(values)
        result_head = solution_func(head)
        result = linked_list_to_list(result_head)
        if result == expected:
            passed += 1
            print(f"PASS | head={values} -> {result}")
        else:
            print(f"FAIL | head={values} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(middle_node_sol1)
    # run_basic_tests(middle_node_sol2)
    # run_basic_tests(middle_node_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
