# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node: BinaryTreeNode):
            if node is None:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res[0] = max(left_max + right_max + node.val, res[0])
            return node.val + max(left_max, right_max)
        dfs(root)
        return res[0]