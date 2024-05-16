# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return
            if node.left and node.right:
                left=dfs(node.left)
                right=dfs(node.right)
            
            if not node.left and not node.right:
                return False if node.val==0 else True
            
            if node.val==2:
                return left or right
            elif node.val==3:
                return left and right
        
        return dfs(root)