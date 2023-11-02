# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)

            total_sum = left_sum + right_sum
            total_cnt = 1 + left_cnt + right_cnt

            if total_sum // total_cnt == node.val:
                self.cnt += 1
            
            return total_sum, total_cnt
    
        dfs(root)
        return self.cnt