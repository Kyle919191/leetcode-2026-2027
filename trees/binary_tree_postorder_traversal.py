"""
LeetCode 145 - Binary Tree Postorder Traversal

Task:
Given the `root` of a binary tree, return the postorder traversal of its nodes'
values.

Postorder order: left -> right -> root.

Example 1:
Input: root = [1, null, 2, 3]
Output: [3, 2, 1]

Example 2:
Input: root = []
Output: []
"""


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
def postorder_traversal_sol1(root: TreeNode | None) -> list[int]:
    result = []

    def traverse(root: TreeNode):
        if root is None:
            return 
        traverse(root.left)
        traverse(root.right)
        result.append(root.val)
        return
    
    traverse(root)
    return result


# Solution 2
# Iterative postorder walkthrough example:
# Tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4  5  6  7
#
# Postorder target: [4, 5, 2, 6, 7, 3, 1]
#
# Core trick:
# 1) Do a modified preorder: root -> right -> left.
# 2) Reverse the result to get: left -> right -> root.
#
# Why this stack order works:
# - We pop from stack (LIFO).
# - If we push left first, then right, right is popped first.
# - So visit order becomes root, right, left.
#
# Snapshot highlights:
# - Start: stack=[1], result=[]
# - Pop 1, append -> result=[1], push 2 then 3
# - Pop 3, append -> result=[1,3], push 6 then 7
# - Pop 7, then 6 -> result=[1,3,7,6]
# - Pop 2, append -> result=[1,3,7,6,2], push 4 then 5
# - Pop 5, then 4 -> result=[1,3,7,6,2,5,4]
# - Reverse -> [4,5,2,6,7,3,1]
def postorder_traversal_sol2(root: TreeNode | None) -> list[int]:
    if root is None:
        return []

    result: list[int] = []
    stack: list[TreeNode] = [root]

    # Preorder variant: root -> right -> left, then reverse.
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    result.reverse()
    return result


# Solution 3 (optional)
def postorder_traversal_sol3(root: TreeNode | None) -> list[int]:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement postorder_traversal_sol3")


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
        ([1, None, 2, 3], [3, 2, 1]),       # example 1
        ([], []),                            # empty tree
        ([1], [1]),                          # single node
        ([1, 2, 3, 4, 5, 6, 7], [4, 5, 2, 6, 7, 3, 1]),
        ([1, 2, None, 3], [3, 2, 1]),        # left chain
        ([1, None, 2, None, 3], [3, 2, 1]),  # right chain
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
    run_basic_tests(postorder_traversal_sol1)
    # run_basic_tests(postorder_traversal_sol2)
    # run_basic_tests(postorder_traversal_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
