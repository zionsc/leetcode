# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node, lst):
            if not node:
                return
            if not node.left and not node.right:
                lst.append(node.val)
            dfs(node.left, lst)
            dfs(node.right, lst)
            return lst
        
        lst1 = dfs(root1, [])
        lst2 = dfs(root2, [])
        
        if lst1 == lst2:
            return True
        return False
        
        
