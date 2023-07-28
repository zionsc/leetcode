# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # returns the index of that value in inorder array

        # treat them as having the values in the same list of indexes, but in different order. so we must cut in 
        # same place for each array.
        root.left = buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root