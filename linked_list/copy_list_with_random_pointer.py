"""
LeetCode 138 - Copy List with Random Pointer

Task:
A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n
brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the `next` and `random` pointer of the new
nodes should point to new nodes in the copied list such that the pointers in
the original list and copied list represent the same list state.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""


class Node:
    def __init__(
        self,
        x: int,
        next: "Node | None" = None,
        random: "Node | None" = None,
    ):
        self.val = x
        self.next = next
        self.random = random


# Solution 1
def copy_random_list_sol1(head: Node | None) -> Node | None:
    old_to_copy = {None: None} # handle the None "node" as some nodes may point to it

    # first pass: resolve value first, create independent nodes
    cur = head
    while cur is not None:
        old_to_copy[cur] = Node(cur.val)
        cur = cur.next
    
    # second pass: resolve .next .random for the new copy list
    cur = head
    while cur is not None:
        copy = old_to_copy[cur]
        copy.next = old_to_copy[cur.next]
        copy.random = old_to_copy[cur.random]
        cur = cur.next
    return old_to_copy[head] # the mapping is the new copied list


# Solution 2
def copy_random_list_sol2(head: Node | None) -> Node | None:
    # TODO: write your second solution
    raise NotImplementedError("Implement copy_random_list_sol2")


# Solution 3 (optional)
def copy_random_list_sol3(head: Node | None) -> Node | None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement copy_random_list_sol3")


def build_random_list(data: list[list[int | None]]) -> Node | None:
    # data format: [[val, random_index_or_None], ...]
    if not data:
        return None

    nodes = [Node(item[0]) for item in data]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, rand_idx) in enumerate(data):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]


def random_list_to_repr(head: Node | None) -> list[list[int | None]]:
    nodes: list[Node] = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next

    index_map = {node: i for i, node in enumerate(nodes)}
    out: list[list[int | None]] = []
    for node in nodes:
        rand_idx = index_map[node.random] if node.random is not None else None
        out.append([node.val, rand_idx])
    return out


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
        ([[1, 1], [2, 1]]),
        ([[3, None], [3, 0], [3, None]]),
        ([]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for data in test_cases:
        head = build_random_list(data)
        copied = solution_func(head)
        result = random_list_to_repr(copied)
        if result == data:
            passed += 1
            print(f"PASS | data={data} -> {result}")
        else:
            print(f"FAIL | data={data} -> got {result}, expected {data}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(copy_random_list_sol1)
    # run_basic_tests(copy_random_list_sol2)
    # run_basic_tests(copy_random_list_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
