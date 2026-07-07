"""
LeetCode 23 - Merge k Sorted Lists

Task:
You are given an array of `k` linked-list heads `lists`, where each linked list
is sorted in ascending order.

Merge all linked lists into one sorted linked list and return its head.

Example 1:
Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]

Example 2:
Input: lists = []
Output: []
"""
import heapq

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def merge_k_lists_sol1(lists: list[ListNode | None]) -> ListNode | None:
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
    # TODO: write your second solution
    raise NotImplementedError("Implement merge_k_lists_sol2")


# Solution 3 (optional)
def merge_k_lists_sol3(lists: list[ListNode | None]) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement merge_k_lists_sol3")


def build_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    cur = dummy
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next


def build_linked_lists(values_lists: list[list[int]]) -> list[ListNode | None]:
    return [build_linked_list(values) for values in values_lists]


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
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1]], [1]),
        ([[1], [0]], [0, 1]),
        ([[1, 2, 2], [1, 1, 2], [2, 6]], [1, 1, 1, 2, 2, 2, 2, 6]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for lists_values, expected in test_cases:
        lists = build_linked_lists(lists_values)
        result_head = solution_func(lists)
        result = linked_list_to_list(result_head)
        if result == expected:
            passed += 1
            print(f"PASS | lists={lists_values} -> {result}")
        else:
            print(f"FAIL | lists={lists_values} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(merge_k_lists_sol1)
    # run_basic_tests(merge_k_lists_sol2)
    # run_basic_tests(merge_k_lists_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
