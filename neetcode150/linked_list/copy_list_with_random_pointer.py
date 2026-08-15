"""
LeetCode 138 - Copy List with Random Pointer
"""


class Node:
    def __init__(self, x: int, next: "Node | None" = None, random: "Node | None" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list_sol1(head: Node | None) -> Node | None:
    # TODO-TALK: I map each old node to its new copy node in a first pass.
    # TODO-TALK: In a second pass, I wire next and random using that mapping.
    # TODO-TALK: This guarantees all copied pointers reference copied nodes, not original nodes.
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
    raise NotImplementedError("Implement copy_random_list_sol2")


def build_random_list(values: list[int], random_indices: list[int | None]) -> Node | None:
    if not values:
        return None
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, ridx in enumerate(random_indices):
        nodes[i].random = None if ridx is None else nodes[ridx]
    return nodes[0]


def serialize_random_list(head: Node | None) -> list[list[int | None]]:
    nodes = []
    index_of = {}
    cur = head
    i = 0
    while cur is not None:
        nodes.append(cur)
        index_of[cur] = i
        cur = cur.next
        i += 1
    out = []
    for node in nodes:
        ridx = None if node.random is None else index_of[node.random]
        out.append([node.val, ridx])
    return out


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([7, 13, 11, 10, 1], [None, 0, 4, 2, 0]),
        ([1, 2], [1, 1]),
        ([], []),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for values, random_indices in test_cases:
        head = build_random_list(values, random_indices)
        copied = solution_func(head)
        got = serialize_random_list(copied)
        expected = [[v, r] for v, r in zip(values, random_indices)]
        if got == expected:
            passed += 1
            print(f"PASS | data={expected}")
        else:
            print(f"FAIL | got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(copy_random_list_sol1)
    # run_basic_tests(copy_random_list_sol2)
    pass
