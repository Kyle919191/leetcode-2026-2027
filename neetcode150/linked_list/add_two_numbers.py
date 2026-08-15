"""
LeetCode 2 - Add Two Numbers
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def add_two_numbers_sol1(
    l1: ListNode | None,
    l2: ListNode | None,
) -> ListNode | None:
    dummy = ListNode(-1)
    p = dummy
    p1, p2 = l1, l2
    carry = 0

    while p1 is not None or p2 is not None or carry > 0: # carry>0 case say last digit for p1+p2>10, need trailing number
        # TODO-TALK: I add the current digits plus carry, just like pen-and-paper addition.
        val = carry
        if p1 is not None: # p1 and p2 can be different length
            val += p1.val
            p1 = p1.next
        if p2 is not None:
            val += p2.val
            p2 = p2.next
        single_digit_val = val % 10 #keep val as single digit, 
        #use another variable so original var is kept, allowing next line to work properly
        # TODO-TALK: I keep only one digit in this node and carry the tens place forward.
        carry = val // 10

        p.next = ListNode(single_digit_val)
        p = p.next
    return dummy.next


# Solution 2


def add_two_numbers_sol2(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    raise NotImplementedError("Implement add_two_numbers_sol2")


def build_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for l1, l2, expected in test_cases:
        got = linked_list_to_list(solution_func(build_linked_list(l1), build_linked_list(l2)))
        if got == expected:
            passed += 1
            print(f"PASS | l1={l1}, l2={l2} -> {got}")
        else:
            print(f"FAIL | l1={l1}, l2={l2} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(add_two_numbers_sol1)
    # run_basic_tests(add_two_numbers_sol2)
    pass
