"""
LeetCode 142 - Linked List Cycle II

Task:
Given the head of a linked list, return the node where the cycle begins.

If there is no cycle, return `None`.

Example 1:
Input: head = [3, 2, 0, -4], pos = 1
Output: tail connects to node index 1

Example 2:
Input: head = [1, 2], pos = -1
Output: no cycle
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Solution 1
def detect_cycle_sol1(head: ListNode | None) -> ListNode | None:
    # conceptual:
    # 1)when slow and fast meet, the distance slow has travelled from head to meeting point is a multiple of the cycle's length(assume equal for simplicity)
    # bc fast travels 2k steps and slow travels k steps, 2k-k has to be a multiple of the cycle
    # 2) see labuladong image: https://labuladong.online/en/algo/essential-technique/linked-list-skills-summary/

    # break logic
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return None
    
    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next
    return slow
    


# Solution 2
def detect_cycle_sol2(head: ListNode | None) -> ListNode | None:
    # TODO: write your second solution
    raise NotImplementedError("Implement detect_cycle_sol2")


# Solution 3 (optional)
def detect_cycle_sol3(head: ListNode | None) -> ListNode | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement detect_cycle_sol3")


def build_cyclic_list(values: list[int], pos: int) -> tuple[ListNode | None, ListNode | None]:
    if not values:
        return None, None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    entry = None
    if pos != -1:
        entry = nodes[pos]
        nodes[-1].next = entry

    return nodes[0], entry


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([3, 2, 0, -4], 1, 2),
        ([1, 2], -1, None),
        ([1], -1, None),
        ([1], 0, 1),
        ([1, 2, 3, 4], 2, 3),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, pos, expected_val in test_cases:
        head, _ = build_cyclic_list(values, pos)
        result_node = solution_func(head)
        result_val = result_node.val if result_node is not None else None

        if result_val == expected_val:
            passed += 1
            print(f"PASS | head={values}, pos={pos} -> {result_val}")
        else:
            print(
                f"FAIL | head={values}, pos={pos} -> got {result_val}, "
                f"expected {expected_val}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(detect_cycle_sol1)
    # run_basic_tests(detect_cycle_sol2)
    # run_basic_tests(detect_cycle_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
