# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.calc_depth(root, 0)

    def calc_depth(self, node: BinaryTreeNode, d: int):
        if not node:
            return d
        d += 1
        return max(self.calc_depth(node.left, d), self.calc_depth(node.right, d))