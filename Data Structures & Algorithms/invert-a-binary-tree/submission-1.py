# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.reverse_tree(root)
        return root
    
    #test
    def reverse_tree(self, node: TreeNode):
        if node:
            node.left, node.right = node.right, node.left
        if node.left:
            self.reverse_tree(node.left)
        if node.right:
            self.reverse_tree(node.right)