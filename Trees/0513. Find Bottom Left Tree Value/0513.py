# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res = [-1, float('inf')]

        def dfs(node, level):
            if not node:
                return
            if level < self.res[1]:
                self.res = [node.val, level]
            
            dfs(node.left, level - 1)
            dfs(node.right, level - 1)
        
        dfs(root, 0)
        return self.res[0]