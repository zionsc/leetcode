# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # must do pre-order because we have to check then iterate because 
        if not q and not p:
            return False
        
        # pre-order traversal because any other method will not iterate left and right in the same
        # speed -> whatever is recursively declared first would go first. 
        if q and p and q.val == p.val:
            return self.isSameTree(p.left, q.left) and self.isSaemTree(p.right, q.right)
    
        else:
            return False