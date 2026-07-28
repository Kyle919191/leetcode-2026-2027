"""
LeetCode 82 - Remove Duplicates from Sorted List II

Task:
Given the head of a sorted linked list, delete all nodes that have duplicate
numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:
Input: head = [1, 2, 3, 3, 4, 4, 5]
Output: [1, 2, 5]

Example 2:
Input: head = [1, 1, 1, 2, 3]
Output: [2, 3]
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def delete_duplicates_ii_sol1(head: ListNode | None) -> ListNode | None:
    dummy1 = ListNode(10000) # of value that's beyond possible range so it's a dummy
    dummy2 = ListNode(10000)
    
    dup_list = dummy1
    uniq_list = dummy2

    p = head # good practice, save the head

    while p is not None: # same general idea as remove dup i, iterate over the entire list
        # Why keep dup_list?
        # - p.next check can only detect "start/middle" of a duplicate run.
        # - It cannot detect the LAST node in a run, e.g. [3,3,3]:
        #   when p is the last 3, p.next is different/None.
        # - dup_list stores duplicate values we've already seen, so
        #   "p.val == dup_list.val" lets us classify that trailing duplicate.

        # remove duplicates i doesn't have this problem because we dont need to delete all duplicate instances
        if (p.next is not None and p.val == p.next.val) or p.val == dup_list.val:
            dup_list.next = p
            dup_list = dup_list.next
        else:
            uniq_list.next = p
            uniq_list = uniq_list.next
        
        p = p.next
        dup_list.next = None # disconnect these two lists from the p list, just like partition_list.py
        uniq_list.next = None

    return dummy2.next

# Solution 2
def delete_duplicates_ii_sol2(head: ListNode | None) -> ListNode | None:
    dummy = ListNode(0, head)
    prev = dummy
    cur = head

    while cur is not None:
        # If current value repeats, skip all nodes with this value.
        if cur.next is not None and cur.val == cur.next.val:
            dup_val = cur.val
            while cur is not None and cur.val == dup_val:
                cur = cur.next
            prev.next = cur
        else:
            prev = cur
            cur = cur.next

    return dummy.next


# Solution 3 (optional)
def delete_duplicates_ii_sol3(head: ListNode | None) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement delete_duplicates_ii_sol3")


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
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
        ([1, 1], []),
        ([1, 2, 2], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        ([1, 1, 2, 2, 3, 3], []),
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
    run_basic_tests(delete_duplicates_ii_sol1)
    # run_basic_tests(delete_duplicates_ii_sol2)
    # run_basic_tests(delete_duplicates_ii_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
