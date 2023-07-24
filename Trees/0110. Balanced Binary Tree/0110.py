# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # must keep track of a height and a bool to check if node is balanced -> children must be balanced as well

        def dfs(root):
            if not root:
                return [0, True]
            
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[1] and right[1] and abs(left - right) <= 1

            return [1 + max(left[0], right[0]), balanced]