# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = 0
        def dfs(node):
            if not node:
                return (0, 0)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1

            self.res = max(self.res, curr_sum / curr_count)

            return (curr_sum, curr_count)

        dfs(root)
        return self.res
            