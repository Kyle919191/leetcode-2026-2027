"""
Reverse First N Nodes of a Linked List

Task:
Given the head of a singly linked list and an integer `n`, reverse only the
first `n` nodes and return the new head.

Example 1:
Input: head = [1, 2, 3, 4, 5], n = 3
Output: [3, 2, 1, 4, 5]

Example 2:
Input: head = [1, 2], n = 1
Output: [1, 2]
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1 (example iterative approach)
def reverse_first_n_sol1(head: ListNode | None, n: int) -> ListNode | None:
    if head is None or head.next is None or n <= 1: #edge case when n=0
        return head

    prev, cur, nxt = None, head, head.next
    while n > 0 and cur is not None: # edge case when n is too big?
        cur.next = prev
        prev = cur
        cur = nxt
        if nxt is not None: #check validity of next, don't care about next.next
            nxt = nxt.next
        n -= 1
    head.next = cur #extra step: link the end of this new reversed list to the start of the still-normal list
    return prev


# Solution 2
def reverse_first_n_sol2(head: ListNode | None, n: int) -> ListNode | None:
    global successor
    if head is None or n <= 0:
        return head
    if n==1:
        successor = head.next
        return head

    remaining = reverse_first_n_sol2(head.next, n-1)
    head.next.next = head
    head.next = successor
    return remaining


# Solution 3 (optional)
def reverse_first_n_sol3(head: ListNode | None, n: int) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement reverse_first_n_sol3")


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
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2], 1, [1, 2]),
        ([1, 2], 2, [2, 1]),
        ([1], 1, [1]),
        ([1, 2, 3], 0, [1, 2, 3]),
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
    #run_basic_tests(reverse_first_n_sol1)
    run_basic_tests(reverse_first_n_sol2)
    # run_basic_tests(reverse_first_n_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
