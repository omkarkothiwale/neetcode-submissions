# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indeces = {val: key for key, val in enumerate(inorder)}
        self.root_index = 0

        def dfs(l, r):
            if l > r:
                return None
            root_val = preorder[self.root_index]
            root = TreeNode(root_val)
            self.root_index += 1
            mid = indeces[root_val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0, len(inorder)-1)