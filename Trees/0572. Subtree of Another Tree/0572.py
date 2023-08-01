# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot is empty, regardless of root, it will always be a valid component of a subtree
        if not subRoot:
            return True
        # if not subRoot didn't catch, it means subRoot is empty, but if root is empty and subRoot exists, it is not valid.
        if not root:
            return False
    
        if self.sameTree(root, subRoot):
            return True
    
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    
    # define a helperfucnt to help determine if this is the same subtree!
    def sameTree(self, r, s):
        if not r and not s:
            return True
        
        if s and r and s.val == r.val:
            return self.sameTree(r.left, s.left) and self.sameTree(r.right, s.right)

        return False