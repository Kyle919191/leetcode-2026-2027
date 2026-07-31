"""
LeetCode 445 - Add Two Numbers II

Task:
You are given two non-empty linked lists representing two non-negative
integers. The most significant digit comes first and each node contains a
single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example 1:
Input: l1 = [7, 2, 4, 3], l2 = [5, 6, 4]
Output: [7, 8, 0, 7]

Example 2:
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [8, 0, 7]
"""

from reverse_linked_list import reverse_list_sol1
from add_two_numbers import add_two_numbers_sol1

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def add_two_numbers_ii_sol1(
    l1: ListNode | None,
    l2: ListNode | None,
) -> ListNode | None:
    # from observation, if reverse two lists, become add two numbers I
    p1 = reverse_list_sol1(l1)
    p2 = reverse_list_sol1(l2)
    result = add_two_numbers_sol1(p1, p2)
    return reverse_list_sol1(result) # need to reverse final result


# Solution 2
def add_two_numbers_ii_sol2(
    l1: ListNode | None,
    l2: ListNode | None,
) -> ListNode | None:
    stack1 = []
    stack2 = []

    # same logic as above really
    # using stack(LIFO) is basically reversing the linked lists
    while l1 is not None:
        stack1.append(l1.val)
        l1 = l1.next
    while l2 is not None:
        stack2.append(l2.val)
        l2 = l2.next   
    
    dummy = ListNode(-1)
    carry = 0
    #then, do same logic as add two numbers i
    while stack1 or stack2 or carry > 0:
        val = carry
        if stack1:
            val += stack1.pop()
        if stack2:
            val += stack2.pop()
        
        single_digit_val = val % 10
        carry = val // 10

        # remember how we reverse the result of the final linked list? we're doing the same here!
        new_node = ListNode(single_digit_val)
        new_node.next = dummy.next # put new node before the already created list to get new list
        dummy.next = new_node # now, dummy points to the first node of the new list
    return dummy.next



# Solution 3 (optional)
def add_two_numbers_ii_sol3(
    l1: ListNode | None,
    l2: ListNode | None,
) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement add_two_numbers_ii_sol3")


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
        ([7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7]),
        ([2, 4, 3], [5, 6, 4], [8, 0, 7]),
        ([0], [0], [0]),
        ([9, 9, 9], [1], [1, 0, 0, 0]),
        ([1], [9, 9, 9], [1, 0, 0, 0]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for l1_vals, l2_vals, expected in test_cases:
        l1 = build_linked_list(l1_vals)
        l2 = build_linked_list(l2_vals)
        result_head = solution_func(l1, l2)
        result = linked_list_to_list(result_head)
        if result == expected:
            passed += 1
            print(f"PASS | l1={l1_vals}, l2={l2_vals} -> {result}")
        else:
            print(
                f"FAIL | l1={l1_vals}, l2={l2_vals} -> "
                f"got {result}, expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    #run_basic_tests(add_two_numbers_ii_sol1)
    run_basic_tests(add_two_numbers_ii_sol2)
    # run_basic_tests(add_two_numbers_ii_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
