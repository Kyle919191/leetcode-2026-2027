"""
LeetCode 206 - Reverse Linked List

Task:
Given the head of a singly linked list, reverse the list and return the new
head.

Example 1:
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Example 2:
Input: head = [1, 2]
Output: [2, 1]
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def reverse_list_sol1(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    
    prev, cur, next = None, head, head.next
    while cur is not None:
        cur.next = prev
        prev = cur
        cur = next
        if next is not None: # it's next not cur.next, because cur.next is already reversed
            next = next.next #it's next.next not cur.next, because cur.next is already reversed
    
    return prev # because the last iteration when cur is not Null, it does cur=next, which means cur = null, so prev is the last node


# Solution 2
def reverse_list_sol2(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    
    rest = reverse_list_sol2(head.next)
    head.next.next = head #fix the pointer of the head.next node
    head.next = None
    return rest # rest is the head node of that reversed linked list


# Solution 3 (optional)
def reverse_list_sol3(head: ListNode | None) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement reverse_list_sol3")


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
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
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
    #run_basic_tests(reverse_list_sol1)
    run_basic_tests(reverse_list_sol2)
    # The recursive and iterative solutions both have time complexity O(N), but the iterative one uses O(1) space, 
    # while the recursive one needs stack space, so its space complexity is O(N).



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
