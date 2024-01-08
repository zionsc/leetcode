# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 
            if node.val >= low and node.val <= high:
                self.res += node.val
            if low < node.val:
                dfs(node.left)
            if high > node.val:
                dfs(node.right)
        dfs(root)
        return self.res
            
