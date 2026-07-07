"""
LeetCode 102 - Binary Tree Level Order Traversal

Task:
Given the `root` of a binary tree, return the level order traversal of its
nodes' values (from left to right, level by level).

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]

Example 2:
Input: root = [1]
Output: [[1]]
"""

from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


# Solution 1
def level_order_sol1(root: TreeNode | None) -> list[list[int]]:

    if root is None:
        return []

    result = []

    def process_levels(level):
        next_level = []
        vals = []
        
        if level == []:
            return
        
        for node in level:
            vals.append(node.val)
            left = node.left
            right = node.right
            if left is not None:
                next_level.append(left)
            if right is not None:
                next_level.append(right)

        result.append(vals)
        process_levels(next_level)
    
    process_levels([root])

    return result


# Solution 2
def level_order_sol2(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    p = deque()
    p.append(root)
    result = []
    depth = 0

    while p:
        level_size = len(p)
        val = []
        for _ in range(level_size):
            node = p.popleft()
            val.append(node.val)
            if node.left is not None:
                p.append(node.left)
            if node.right is not None:
                p.append(node.right)
        result.append(val)
        depth += 1
    return result

# Solution 3 (optional)
def level_order_sol3(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []

    class State:
        def __init__(self, node: TreeNode, depth: int):
            self.node = node
            self.depth = depth

    q = deque([State(root, 0)])
    result: list[list[int]] = []

    while q:
        cur = q.popleft()

        # First time we reach this depth, create a new bucket.
        if cur.depth == len(result):
            result.append([])
        result[cur.depth].append(cur.node.val)

        if cur.node.left is not None:
            q.append(State(cur.node.left, cur.depth + 1))
        if cur.node.right is not None:
            q.append(State(cur.node.right, cur.depth + 1))

    return result


def build_tree_from_level_order(values: list[int | None]) -> TreeNode | None:
    if not values:
        return None
    if values[0] is None:
        return None

    nodes: list[TreeNode | None] = [
        TreeNode(v) if v is not None else None for v in values
    ]
    child = 1
    for i in range(len(values)):
        if nodes[i] is None:
            continue
        if child < len(values):
            nodes[i].left = nodes[child]
            child += 1
        if child < len(values):
            nodes[i].right = nodes[child]
            child += 1
    return nodes[0]


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),  # example 1
        ([1], [[1]]),                                               # example 2
        ([], []),                                                   # empty tree
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
        ([1, 2, None, 3], [[1], [2], [3]]),                         # left chain
        ([1, None, 2, None, 3], [[1], [2], [3]]),                   # right chain
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for values, expected in test_cases:
        root = build_tree_from_level_order(values)
        result = solution_func(root)
        if result == expected:
            passed += 1
            print(f"PASS | root={values} -> {result}")
        else:
            print(f"FAIL | root={values} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    #run_basic_tests(level_order_sol1)
    run_basic_tests(level_order_sol2)
    # run_basic_tests(level_order_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
