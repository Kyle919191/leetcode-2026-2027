"""
LeetCode 83 - Remove Duplicates from Sorted List

Task:
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once.

Return the linked list sorted as well.

Example 1:
Input: head = [1, 1, 2]
Output: [1, 2]

Example 2:
Input: head = [1, 1, 2, 3, 3]
Output: [1, 2, 3]
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def delete_duplicates_sol1(head: ListNode | None) -> ListNode | None:
    cur = head
    while cur is not None and cur.next is not None:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next # must wrap this in else loop, because we only want to advance when we're free of duplicates
            # each time we do cur=cur.next it has to be a distinct node
    return head


# Solution 2
def delete_duplicates_sol2(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head # if it's empty node or 1 node, it's always distinct
    
    head.next = delete_duplicates_sol2(head.next)

    if head.next is not None and head.val == head.next.val: # the actual logic of recursion
        return head.next #we guanrantee the remaning list is distinct, but we need to explicitly
        # handle the case where the first node is not distinct with rest of list
    return head


# Solution 3 (optional)
def delete_duplicates_sol3(head: ListNode | None) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement delete_duplicates_sol3")


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
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([1], [1]),
        ([], []),
        ([1, 1, 1, 1], [1]),
        ([1, 2, 3], [1, 2, 3]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, expected in test_cases:
        head = build_linked_list(values)
        result_head = solution_func(head)
        result = linked_list_to_list(result_head)
        if result == expected:
            passed += 1
            print(f"PASS | head={values} -> {result}")
        else:
            print(f"FAIL | head={values} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    #run_basic_tests(delete_duplicates_sol1)
    run_basic_tests(delete_duplicates_sol2)
    # run_basic_tests(delete_duplicates_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
