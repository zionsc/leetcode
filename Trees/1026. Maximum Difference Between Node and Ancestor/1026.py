# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, curr_max, curr_min):
            if not node:
                return
            
            self.res = max(self.res, abs(node.val - curr_max), abs(node.val - curr_min))

            new_max = max(node.val, curr_max)
            new_min = min(node.val, curr_min)

            dfs(node.left, new_max, new_min)
            dfs(node.right, new_max, new_min)

        dfs(root, root.val, root.val)
        return self.res