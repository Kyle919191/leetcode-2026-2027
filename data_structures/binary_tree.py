class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


# -------------------------------
# 1) Node-based binary tree
# -------------------------------
# You can build a binary tree like this:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

# The constructed binary tree looks like this:
#     1
#    / \
#   2   3
#  /   / \
# 4   5   6


# -------------------------------
# 2) Dictionary-based tree
# -------------------------------
# 1 -> [2, 3]
# 2 -> [4]
# 3 -> [5, 6]
tree = {
    1: [2, 3],
    2: [4],
    3: [5, 6],
}


# ---------------------------------------------------------------------------------------------