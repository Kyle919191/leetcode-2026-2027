"""
LeetCode 141 - Linked List Cycle

Task:
Given `head`, the head of a linked list, determine if the linked list has a
cycle in it.

Return `True` if there is a cycle in the linked list. Otherwise, return
`False`.

Example 1:
Input: head = [3, 2, 0, -4], pos = 1
Output: True

Example 2:
Input: head = [1, 2], pos = -1
Output: False
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def has_cycle_sol1(head: ListNode | None) -> bool:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


# Solution 2
def has_cycle_sol2(head: ListNode | None) -> bool:
    # TODO: write your second solution
    raise NotImplementedError("Implement has_cycle_sol2")


# Solution 3 (optional)
def has_cycle_sol3(head: ListNode | None) -> bool:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement has_cycle_sol3")


def build_cyclic_list(values: list[int], pos: int) -> ListNode | None:
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], -1, False),
        ([1], -1, False),
        ([1], 0, True),
        ([1, 2, 3], 0, True),
        ([1, 2, 3], -1, False),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, pos, expected in test_cases:
        head = build_cyclic_list(values, pos)
        result = solution_func(head)
        if result == expected:
            passed += 1
            print(f"PASS | head={values}, pos={pos} -> {result}")
        else:
            print(
                f"FAIL | head={values}, pos={pos} -> got {result}, "
                f"expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(has_cycle_sol1)
    # run_basic_tests(has_cycle_sol2)
    # run_basic_tests(has_cycle_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
