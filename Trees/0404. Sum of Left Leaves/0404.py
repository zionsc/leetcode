# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            sm = dfs(node.left) + dfs(node.right)
            if node.left and not node.left.left and not node.left.right:
                sm += node.left.val
            return sm
        return dfs(root)