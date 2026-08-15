"""
LeetCode 25 - Reverse Nodes in k-Group
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


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


def reverse_k_group_sol1(head: ListNode | None, k: int) -> ListNode | None:
    a = b = head
    for _ in range (k):
        if b is None: # make sure b is accessible first
            # TODO-TALK: Fewer than k nodes remain, so this tail stays as-is.
            return head
        b = b.next
    # TODO-TALK: I reverse the first k nodes and connect its tail to the recursive result.
    newHead = reverse_first_n_sol1(a, k)
    a.next = reverse_k_group_sol1(b, k)
    return newHead #return the head of this new list


# Solution 2


def reverse_k_group_sol2(head: ListNode | None, k: int) -> ListNode | None:
    raise NotImplementedError("Implement reverse_k_group_sol2")


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
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2], 3, [1, 2]),
        ([], 2, []),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for values, k, expected in test_cases:
        got = linked_list_to_list(solution_func(build_linked_list(values), k))
        if got == expected:
            passed += 1
            print(f"PASS | head={values}, k={k} -> {got}")
        else:
            print(f"FAIL | head={values}, k={k} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(reverse_k_group_sol1)
    # run_basic_tests(reverse_k_group_sol2)
    pass
