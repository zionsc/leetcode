# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    
    # define a helperfucnt to help determine if this is the same subtree!
    def sameTree(self, r, s):
        if not r and not s:
            return True
        
        if s and r and s.val == r.val:
            return self.sameTree(r.left, s.left) and self.sameTree(r.right, s.right)

        return False