"""
LeetCode 94 - Binary Tree Inorder Traversal

Task:
Given the `root` of a binary tree, return the inorder traversal of its nodes'
values.

Inorder order: left -> root -> right.

Example 1:
Input: root = [1, null, 2, 3]
Output: [1, 3, 2]

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
def inorder_traversal_sol1(root: TreeNode | None) -> list[int]:
    result = []

    def traverse(root: TreeNode):
        if root is None:
            return 
        traverse(root.left)
        result.append(root.val)
        traverse(root.right)
        return
    
    traverse(root)
    return result


# Solution 2
# Iterative inorder walkthrough example:
# Tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4  5  6  7
#
# Inorder target: [4, 2, 5, 1, 6, 3, 7]
#
# Core idea:
# 1) Keep going left, pushing nodes onto stack.
# 2) When no left exists, pop, visit node.
# 3) Move to its right child, repeat.
#
# Snapshot highlights:
# - Start: cur=1, stack=[], result=[]
# - Push left chain 1->2->4: stack=[1,2,4], cur=None
# - Pop/visit 4: result=[4]
# - Pop/visit 2, then go right to 5: result=[4,2]
# - Visit 5: result=[4,2,5]
# - Pop/visit 1, then go right to 3: result=[4,2,5,1]
# - Repeat on 3's left chain (3->6), then 3, then 7
# - Final: result=[4,2,5,1,6,3,7]
def inorder_traversal_sol2(root: TreeNode | None) -> list[int]:
    result: list[int] = []
    stack: list[TreeNode] = []
    cur = root

    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            # building the left backbone
            cur = cur.left
        
        #since the left backbone is built in the stack, we now just
        #treat the left most leaf 4 as a middle node, visit, right is None
        # now second pop stack means 2's left branch is done
        # visit middle node(2), then visit right: if right is not None, try building the
        # left backbone starting from that (for exmaple 3, 6)
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right

    return result


# Solution 3 (optional)
def inorder_traversal_sol3(root: TreeNode | None) -> list[int]:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement inorder_traversal_sol3")


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
        ([1, None, 2, 3], [1, 3, 2]),       # example 1
        ([], []),                            # empty tree
        ([1], [1]),                          # single node
        ([1, 2, 3, 4, 5, 6, 7], [4, 2, 5, 1, 6, 3, 7]),
        ([1, 2, None, 3], [3, 2, 1]),        # left chain
        ([1, None, 2, None, 3], [1, 2, 3]),  # right chain
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
    #run_basic_tests(inorder_traversal_sol1)
    run_basic_tests(inorder_traversal_sol2)
    # run_basic_tests(inorder_traversal_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
