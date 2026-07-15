"""
LeetCode 160 - Intersection of Two Linked Lists

Task:
Given the heads of two singly linked-lists `headA` and `headB`, return the
node at which the two lists intersect.

If the two linked lists have no intersection, return `None`.

Example 1:
Input: listA = [4, 1, 8, 4, 5], listB = [5, 6, 1, 8, 4, 5], intersectVal = 8
Output: node with value 8

Example 2:
Input: listA = [1, 2, 3], listB = [4, 5], intersectVal = 0
Output: None
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def get_intersection_node_sol1(
    headA: ListNode | None,
    headB: ListNode | None,
) -> ListNode | None:
    
    p1 = headA
    p2 = headB
    p1_length = 1
    p2_length = 1

    while p1 is not None:
        p1_length += 1
        p1 = p1.next
    while p2 is not None:
        p2_length += 1
        p2 = p2.next
    
    if p1_length >= p2_length:
        for i in range (p1_length-p2_length):
            headA = headA.next
    else:
        for i in range (p2_length-p1_length):
            headB = headB.next
            
    # check if the two pointers are the same, there are two cases when p1 == p2:
    # 1. either the two linked lists do not intersect and both reach the end null pointer
    # 2. or the two linked lists intersect and they reach the intersection point
    while headA != headB:
        headA = headA.next
        headB = headB.next
    return headA


# Solution 2
def get_intersection_node_sol2(
    headA: ListNode | None,
    headB: ListNode | None,
) -> ListNode | None:
    # TODO: write your second solution
    raise NotImplementedError("Implement get_intersection_node_sol2")


# Solution 3 (optional)
def get_intersection_node_sol3(
    headA: ListNode | None,
    headB: ListNode | None,
) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement get_intersection_node_sol3")


def build_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    cur = dummy
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next


def build_intersection_lists(
    a_prefix: list[int],
    b_prefix: list[int],
    shared: list[int],
) -> tuple[ListNode | None, ListNode | None]:
    shared_head = build_linked_list(shared)

    headA = build_linked_list(a_prefix)
    headB = build_linked_list(b_prefix)

    if headA is None:
        headA = shared_head
    else:
        tailA = headA
        while tailA.next is not None:
            tailA = tailA.next
        tailA.next = shared_head

    if headB is None:
        headB = shared_head
    else:
        tailB = headB
        while tailB.next is not None:
            tailB = tailB.next
        tailB.next = shared_head

    return headA, headB


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([4, 1], [5, 6, 1], [8, 4, 5], 8),
        ([1, 9, 1], [3], [2, 4], 2),
        ([1, 2, 3], [4, 5], [], None),
        ([], [], [7, 8], 7),
        ([1], [2], [], None),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for a_prefix, b_prefix, shared, expected_val in test_cases:
        headA, headB = build_intersection_lists(a_prefix, b_prefix, shared)
        result_node = solution_func(headA, headB)
        result_val = result_node.val if result_node is not None else None

        if result_val == expected_val:
            passed += 1
            print(
                f"PASS | A={a_prefix}+{shared}, B={b_prefix}+{shared} "
                f"-> {result_val}"
            )
        else:
            print(
                f"FAIL | A={a_prefix}+{shared}, B={b_prefix}+{shared} "
                f"-> got {result_val}, expected {expected_val}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(get_intersection_node_sol1)
    # run_basic_tests(get_intersection_node_sol2)
    # run_basic_tests(get_intersection_node_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
