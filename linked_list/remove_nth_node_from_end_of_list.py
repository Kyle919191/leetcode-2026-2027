"""
LeetCode 19 - Remove Nth Node From End of List

Task:
Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Example 1:
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]

Example 2:
Input: head = [1], n = 1
Output: []
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

# Solution 1
def remove_nth_from_end_sol1(head: ListNode | None, n: int) -> ListNode | None:
    if head is None:
        return None
    dummy = ListNode(-1)
    dummy.next = head
    # first find n+1 th node from end
    p1 = _find_from_end(dummy, n + 1) # have to call with dummy, not head
    p1.next = p1.next.next
    return dummy.next


# Solution 2
def remove_nth_from_end_sol2(head: ListNode | None, n: int) -> ListNode | None:
    # TODO: write your second solution
    raise NotImplementedError("Implement remove_nth_from_end_sol2")


# Solution 3 (optional)
def remove_nth_from_end_sol3(head: ListNode | None, n: int) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement remove_nth_from_end_sol3")


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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, n, expected in test_cases:
        head = build_linked_list(values)
        result_head = solution_func(head, n)
        result = linked_list_to_list(result_head)
        if result == expected:
            passed += 1
            print(f"PASS | head={values}, n={n} -> {result}")
        else:
            print(
                f"FAIL | head={values}, n={n} -> got {result}, "
                f"expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(remove_nth_from_end_sol1)
    # run_basic_tests(remove_nth_from_end_sol2)
    # run_basic_tests(remove_nth_from_end_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
