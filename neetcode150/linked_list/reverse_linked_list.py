"""
LeetCode 206 - Reverse Linked List
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def reverse_list_sol1(head: ListNode | None) -> ListNode | None:
    # TODO-TALK: I reverse pointers in place with three references: prev, cur, and next.
    # TODO-TALK: Each step flips one arrow, then moves all pointers forward.
    # TODO-TALK: At the end, prev is the new head.
    if head is None or head.next is None:
        return head
    
    prev, cur, next = None, head, head.next
    while cur is not None:
        cur.next = prev
        prev = cur
        cur = next
        if next is not None: # it's next not cur.next, because cur.next is already reversed
            next = next.next #it's next.next not cur.next, because cur.next is already reversed
    
    return prev # because the last iteration when cur is not Null, it does cur=next, which means cur = null, so prev is the last node


# Solution 2


def reverse_list_sol2(head: ListNode | None) -> ListNode | None:
    raise NotImplementedError("Implement reverse_list_sol2")


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
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for values, expected in test_cases:
        result = solution_func(build_linked_list(values))
        got = linked_list_to_list(result)
        if got == expected:
            passed += 1
            print(f"PASS | head={values} -> {got}")
        else:
            print(f"FAIL | head={values} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(reverse_list_sol1)
    # run_basic_tests(reverse_list_sol2)
    pass
