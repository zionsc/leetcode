# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
            
        self.res=[]
        def dfs(node,currString):
            if not node.left and not node.right:
                currString+=chr(node.val+ord('a'))
                self.res.append(currString[::-1])
                return
            currString+=chr(node.val+ord('a'))
            if node.left:
                dfs(node.left,currString)
            if node.right:
                dfs(node.right,currString)
        
        dfs(root,"")
        return sorted(self.res)[0]