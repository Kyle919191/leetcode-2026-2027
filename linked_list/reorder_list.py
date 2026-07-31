"""
LeetCode 143 - Reorder List

Task:
You are given the head of a singly linked list:
L0 -> L1 -> ... -> Ln - 1 -> Ln

Reorder it to:
L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...

You may not modify the values in the list's nodes. Only nodes themselves may be
changed.

Example 1:
Input: head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]

Example 2:
Input: head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]
"""

from middle_of_the_linked_list import middle_node_sol1

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def reorder_list_sol1(head: ListNode | None) -> None:
    if head is None or head.next is None:
        return

    middle = middle_node_sol1(head)


    second_half = middle.next
    middle.next = None
    if second_half is None:
        return

    # Reverse the second half in-place (start after middle).
    prev, cur, nxt = None, second_half, second_half.next
    while cur is not None:
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
        tmp1 = p1.next
        tmp2 = p2.next

        p1.next = p2
        p2.next = tmp1

        p1 = tmp1
        p2 = tmp2






# Solution 2
def reorder_list_sol2(head: ListNode | None) -> None:
    # TODO: write your second solution (modify in-place, return None)
    raise NotImplementedError("Implement reorder_list_sol2")


# Solution 3 (optional)
def reorder_list_sol3(head: ListNode | None) -> None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement reorder_list_sol3")


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
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, expected in test_cases:
        head = build_linked_list(values)
        solution_func(head)  # in-place
        result = linked_list_to_list(head)
        if result == expected:
            passed += 1
            print(f"PASS | head={values} -> {result}")
        else:
            print(f"FAIL | head={values} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(reorder_list_sol1)
    # run_basic_tests(reorder_list_sol2)
    # run_basic_tests(reorder_list_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
