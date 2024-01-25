# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if node == q or node == p:
                return node
        
            if left and right:
                return node
            elif left or right:
                return left or right
        
        return dfs(root)
