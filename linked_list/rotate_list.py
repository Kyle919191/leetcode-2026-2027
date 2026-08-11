"""
LeetCode 61 - Rotate List

Task:
Given the head of a linked list, rotate the list to the right by `k` places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""


from reverse_linked_list import reverse_list_sol1


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def rotate_right_sol1(head: ListNode | None, k: int) -> ListNode | None:
    if head is None or head.next is None or k == 0:
        return head

    # First pass: get list length and tail.
    n = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        n += 1

    # Rotating by n is a no-op.
    k %= n
    if k == 0:
        return head

    # Make it circular, then cut at the new tail.
    tail.next = head
    steps_to_new_tail = n - k - 1
    new_tail = head
    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head


# Solution 2
def rotate_right_sol2(head: ListNode | None, k: int) -> ListNode | None:
    if head is None or head.next is None or k == 0:
        return head
    
    n = 0
    cur = head
    while cur is not None:
        n += 1
        cur = cur.next
    
    k = k % n # rotating right by 4 for a length 3 list is the same as rotating right by 1
    if k == 0:
        return head
    
    # Reverse whole list.
    # Example: head = 1->2->3->4->5, k = 2
    # After reversing whole list:
    # rev_head = 5->4->3->2->1
    rev_head = reverse_list_sol1(head)

    lst1 = rev_head
    cur = lst1

    # Split first k nodes and the remaining n-k nodes.
    # For the example, k = 2:
    # first part:  5->4
    # second part: 3->2->1
    for _ in range(k-1):
        cur = cur.next
    lst2 = cur.next
    cur.next = None # isloate two lists

    # Reverse each part back.
    # reverse(first part):  5->4      -> 4->5
    # reverse(second part): 3->2->1   -> 1->2->3
    # connect them: 4->5->1->2->3
    # which is exactly rotating original list right by 2.
    lst1_rev = reverse_list_sol1(lst1)
    tail = lst1 # first reversed's head(5) now becomes the tail that connects to second part
    tail.next = reverse_list_sol1(lst2)
    return lst1_rev




# Solution 3 (optional)
def rotate_right_sol3(head: ListNode | None, k: int) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement rotate_right_sol3")


def build_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    out = []
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
    return out


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
        ([1], 0, [1]),
        ([1], 5, [1]),
        ([], 3, []),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, k, expected in test_cases:
        head = build_linked_list(values)
        result = solution_func(head, k)
        got = linked_list_to_list(result)
        if got == expected:
            passed += 1
            print(f"PASS | head={values}, k={k} -> {got}")
        else:
            print(
                f"FAIL | head={values}, k={k} -> got {got}, expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(rotate_right_sol1)
    # run_basic_tests(rotate_right_sol2)
    # run_basic_tests(rotate_right_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
