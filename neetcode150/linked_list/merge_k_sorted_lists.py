"""
LeetCode 23 - Merge k Sorted Lists
"""

import heapq


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def merge_k_lists_sol1(lists: list[ListNode | None]) -> ListNode | None:
    # TODO-TALK: This is k-way merge with a min-heap.
    # TODO-TALK: I push each list head first, then repeatedly pop the smallest node.
    # TODO-TALK: After popping one node, I push its next node from the same list.
    # edge case 1
    if lists == []:
        return None

    dummy = ListNode(-1)
    start = dummy
    pq = []
    for i, node in enumerate(lists):
        # edge case 2
        if node is not None:
            heapq.heappush(pq, (node.val, i, node))
    
    while pq:
        value, index, node_x = heapq.heappop(pq)
        # edge case 3
        if node_x.next is not None:
            heapq.heappush(pq, (node_x.next.val, index, node_x.next))
        start.next = node_x
        start = start.next
    return dummy.next


# Solution 2


def merge_k_lists_sol2(lists: list[ListNode | None]) -> ListNode | None:
    raise NotImplementedError("Implement merge_k_lists_sol2")


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
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for lists, expected in test_cases:
        built = [build_linked_list(v) for v in lists]
        got = linked_list_to_list(solution_func(built))
        if got == expected:
            passed += 1
            print(f"PASS | lists={lists} -> {got}")
        else:
            print(f"FAIL | lists={lists} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(merge_k_lists_sol1)
    # run_basic_tests(merge_k_lists_sol2)
    pass
