"""
LeetCode 21 - Merge Two Sorted Lists
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def merge_two_lists_sol1(
    list1: ListNode | None,
    list2: ListNode | None,
) -> ListNode | None: 

    # TODO-TALK: I start with a dummy node so attaching nodes stays uniform.
    dummy = ListNode(-1)
    p = dummy

    while list1 is not None and list2 is not None:
        # TODO-TALK: I compare both front values and attach the smaller node first.
        if list1.val < list2.val:
            p.next = list1
            list1 = list1.next
        else:
            p.next = list2
            list2 = list2.next
        p = p.next
        p.next = None
    if list1 is None:
        # TODO-TALK: One list ended, so I append the remaining nodes from the other list.
        p.next = list2
    if list2 is None:
        p.next = list1
    return dummy.next

# Solution 2


def merge_two_lists_sol2(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    raise NotImplementedError("Implement merge_two_lists_sol2")


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
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([5], [], [5]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for v1, v2, expected in test_cases:
        result = solution_func(build_linked_list(v1), build_linked_list(v2))
        got = linked_list_to_list(result)
        if got == expected:
            passed += 1
            print(f"PASS | list1={v1}, list2={v2} -> {got}")
        else:
            print(f"FAIL | list1={v1}, list2={v2} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(merge_two_lists_sol1)
    # run_basic_tests(merge_two_lists_sol2)
    pass
