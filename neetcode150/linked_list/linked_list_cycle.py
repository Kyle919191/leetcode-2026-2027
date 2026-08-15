"""
LeetCode 141 - Linked List Cycle
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def has_cycle_sol1(head: ListNode | None) -> bool:
    # TODO-TALK: I use slow and fast pointers.
    # TODO-TALK: If there is a cycle, fast eventually laps slow and they meet.
    # TODO-TALK: If fast reaches null, the list ends and there is no cycle.
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
    raise NotImplementedError("Implement has_cycle_sol2")


def build_linked_list(values: list[int], pos: int) -> ListNode | None:
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for values, pos, expected in test_cases:
        head = build_linked_list(values, pos)
        got = solution_func(head)
        if got == expected:
            passed += 1
            print(f"PASS | head={values}, pos={pos} -> {got}")
        else:
            print(f"FAIL | head={values}, pos={pos} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(has_cycle_sol1)
    # run_basic_tests(has_cycle_sol2)
    pass
