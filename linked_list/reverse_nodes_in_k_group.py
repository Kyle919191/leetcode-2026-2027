"""
LeetCode 25 - Reverse Nodes in k-Group

Task:
Given the head of a linked list, reverse the nodes of the list `k` at a time,
and return the modified list.

`k` is a positive integer and is less than or equal to the length of the list.
If the number of nodes is not a multiple of `k`, then left-out nodes at the end
should remain as-is.

Example 1:
Input: head = [1, 2, 3, 4, 5], k = 2
Output: [2, 1, 4, 3, 5]

Example 2:
Input: head = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def reverse_k_group_sol1(head: ListNode | None, k: int) -> ListNode | None:
    # TODO: write your first solution
    raise NotImplementedError("Implement reverse_k_group_sol1")


# Solution 2
def reverse_k_group_sol2(head: ListNode | None, k: int) -> ListNode | None:
    # TODO: write your second solution
    raise NotImplementedError("Implement reverse_k_group_sol2")


# Solution 3 (optional)
def reverse_k_group_sol3(head: ListNode | None, k: int) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement reverse_k_group_sol3")


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
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3], 1, [1, 2, 3]),
        ([1, 2, 3], 4, [1, 2, 3]),
        ([1, 2, 3, 4], 2, [2, 1, 4, 3]),
        ([], 2, []),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, k, expected in test_cases:
        head = build_linked_list(values)
        result_head = solution_func(head, k)
        result = linked_list_to_list(result_head)
        if result == expected:
            passed += 1
            print(f"PASS | head={values}, k={k} -> {result}")
        else:
            print(
                f"FAIL | head={values}, k={k} -> got {result}, expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(reverse_k_group_sol1)
    # run_basic_tests(reverse_k_group_sol2)
    # run_basic_tests(reverse_k_group_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
