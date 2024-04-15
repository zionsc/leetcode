# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, currNum):
            if not node.left and not node.right:
                return node.val + currNum
            res=0
            if node.left:
                res+=dfs(node.left, (node.val+currNum)*10)
            if node.right:
                res+=dfs(node.right, (node.val+currNum)*10)
            return res
            
        return dfs(root,0)
            