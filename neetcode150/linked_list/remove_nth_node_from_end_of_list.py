"""
LeetCode 19 - Remove Nth Node From End of List
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def _find_from_end(head: ListNode, k: int) -> ListNode:
    p1 = head
    for i in range (k):
        p1 = p1.next
    p2 = head
    while p1 != None:
        p1 = p1.next
        p2 = p2.next
    
    # # alternatively do
    # p1 = head
    # # now we're at the kth node from the front
    # for i in range (k-1):
    #     p1 = p1.next
    # while p1.next != None:
    #     p1 = p1.next
    #     p2 = p2.next
    return p2


def remove_nth_from_end_sol1(head: ListNode | None, n: int) -> ListNode | None:
    if head is None:
        return None
    # TODO-TALK: I use a dummy node so deleting the original head is handled the same way.
    dummy = ListNode(-1)
    dummy.next = head
    # first find n+1 th node from end
    # TODO-TALK: I locate the node right before the node to delete.
    p1 = _find_from_end(dummy, n + 1) # have to call with dummy, not head
    # TODO-TALK: I remove nth node from end by bypassing it.
    p1.next = p1.next.next
    return dummy.next


# Solution 2


def remove_nth_from_end_sol2(head: ListNode | None, n: int) -> ListNode | None:
    raise NotImplementedError("Implement remove_nth_from_end_sol2")


def build_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for values, n, expected in test_cases:
        got = linked_list_to_list(solution_func(build_linked_list(values), n))
        if got == expected:
            passed += 1
            print(f"PASS | head={values}, n={n} -> {got}")
        else:
            print(f"FAIL | head={values}, n={n} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(remove_nth_from_end_sol1)
    # run_basic_tests(remove_nth_from_end_sol2)
    pass
