"""
LeetCode 143 - Reorder List
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def middle_node_sol1(head: ListNode | None) -> ListNode | None:
    if head is None:
        return None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def reorder_list_sol1(head: ListNode | None) -> None:
    if head is None or head.next is None:
        return

    # TODO-TALK: First I find the middle so I can split the list into two halves.
    middle = middle_node_sol1(head)


    second_half = middle.next
    # TODO-TALK: I cut the list into two independent chains here.
    middle.next = None
    if second_half is None:
        return

    # Reverse the second half in-place (start after middle).
    prev, cur, nxt = None, second_half, second_half.next
    while cur is not None:
        # TODO-TALK: I reverse the second half in place.
        cur.next = prev
        prev = cur
        cur = nxt
        if nxt is not None:
            nxt = nxt.next

    # Merge first half and reversed second half alternately.
    p1 = head
    p2 = prev # prev: new head of the reversed second part
    # Example:
    # first half:   1 -> 2 -> 3
    # second half:  5 -> 4
    #
    # Iteration 1:
    # p1=1, p2=5, tmp1=2, tmp2=4
    # 1->5 and 5->2, list becomes: 1 -> 5 -> 2 -> 3
    # move p1=2, p2=4
    #
    # Iteration 2:
    # p1=2, p2=4, tmp1=3, tmp2=None
    # 2->4 and 4->3, list becomes: 1 -> 5 -> 2 -> 4 -> 3
    # move p1=3, p2=None (stop)
    while p2 is not None:
        # TODO-TALK: Now I weave one node from first half, one node from reversed second half.
        tmp1 = p1.next
        tmp2 = p2.next

        p1.next = p2
        p2.next = tmp1

        p1 = tmp1
        p2 = tmp2






# Solution 2


def reorder_list_sol2(head: ListNode | None) -> None:
    raise NotImplementedError("Implement reorder_list_sol2")


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
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for values, expected in test_cases:
        head = build_linked_list(values)
        solution_func(head)
        got = linked_list_to_list(head)
        if got == expected:
            passed += 1
            print(f"PASS | head={values} -> {got}")
        else:
            print(f"FAIL | head={values} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(reorder_list_sol1)
    # run_basic_tests(reorder_list_sol2)
    pass
