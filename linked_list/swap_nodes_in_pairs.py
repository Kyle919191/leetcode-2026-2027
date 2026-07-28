"""
LeetCode 24 - Swap Nodes in Pairs

Task:
Given a linked list, swap every two adjacent nodes and return its head.

You must solve the problem without modifying node values (only nodes
themselves may be changed).

Example 1:
Input: head = [1, 2, 3, 4]
Output: [2, 1, 4, 3]

Example 2:
Input: head = []
Output: []
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def swap_pairs_sol1(head: ListNode | None) -> ListNode | None:
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy

    while prev.next is not None and prev.next.next is not None:
        a = prev.next
        b = prev.next.next

        prev.next = b
        a.next = b.next # do this before b.next = a, otherwise original b.next is lost
        b.next = a

        prev = a # mve forward one, right before the next pair

    return dummy.next


# Solution 2
def swap_pairs_sol2(head: ListNode | None) -> ListNode | None:
    # TODO: write your second solution
    raise NotImplementedError("Implement swap_pairs_sol2")


# Solution 3 (optional)
def swap_pairs_sol3(head: ListNode | None) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement swap_pairs_sol3")


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
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
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
    run_basic_tests(swap_pairs_sol1)
    # run_basic_tests(swap_pairs_sol2)
    # run_basic_tests(swap_pairs_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
