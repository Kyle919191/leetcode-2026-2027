"""
LeetCode 86 - Partition List

Task:
Given the head of a linked list and an integer `x`, partition the list so that
all nodes with values less than `x` come before nodes with values greater than
or equal to `x`.

You must preserve the original relative order of the nodes in each partition.

Example 1:
Input: head = [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]

Example 2:
Input: head = [2, 1], x = 2
Output: [1, 2]
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def partition_list_sol1(head: ListNode | None, x: int) -> ListNode | None:
    dummy1 = ListNode(-1)
    dummy2 = ListNode(-1)
    list1 = dummy1
    list2 = dummy2

    while head is not None:
        if head.val < x:
            list1.next = head
            head = head.next
            list1 = list1.next
            list1.next = None
        else: 
            list2.next = head
            head = head.next
            list2 = list2.next
            list2.next = None
    
    list1.next = dummy2.next
    return dummy1.next



# Solution 2
def partition_list_sol2(head: ListNode | None, x: int) -> ListNode | None:
    dummy1 = ListNode(-1)
    dummy2 = ListNode(-1)
    list1 = dummy1
    list2 = dummy2

    while head is not None:
        if head.val < x:
            list1.next = head
            list1 = list1.next
        else: 
            list2.next = head
            list2 = list2.next
        # cannot directly move the p pointer forward,
        # p = p.next
        # break the next pointer of each node in the original list
        temp = head.next
        head.next = None
        head = temp

    list1.next = dummy2.next
    return dummy1.next


# Solution 3 (optional)
def partition_list_sol3(head: ListNode | None, x: int) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement partition_list_sol3")


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
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([2, 1], 2, [1, 2]),
        ([], 3, []),
        ([1], 2, [1]),
        ([3, 1, 2], 3, [1, 2, 3]),
        ([4, 5, 1, 2], 3, [1, 2, 4, 5]),
        ([1, 1, 1], 2, [1, 1, 1]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, x, expected in test_cases:
        head = build_linked_list(values)
        result_head = solution_func(head, x)
        result = linked_list_to_list(result_head)
        if result == expected:
            passed += 1
            print(f"PASS | head={values}, x={x} -> {result}")
        else:
            print(
                f"FAIL | head={values}, x={x} -> got {result}, "
                f"expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    #run_basic_tests(partition_list_sol1)
    run_basic_tests(partition_list_sol2)
    # run_basic_tests(partition_list_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
