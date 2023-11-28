# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        self.res = False

        def dfs(node, curr_sum):
            if not node:
                return 
            curr_sum += node.val
            if curr_sum == targetSum and not node.left and not node.right:
                self.res = True
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

        dfs(root, 0)
        return self.res