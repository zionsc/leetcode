# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is basically the heights of l + r, not the height of the current node which would be
        # l + r + 1. For this reason, we need to keep track of a height and a diameter, and since the
        # max diameter could be anywhere in the tree, we need to max() it every time. 

        diameter = 0

        # you can't directly pass something by reference in python, so the easiest method of keeping
        # track of a diameter is to make the function inside of the solution function
        def dfs(root):
            # to say that it is a global function
            nonlocal diameter

