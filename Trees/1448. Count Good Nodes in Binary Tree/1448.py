# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # can use DFS, keep track of a maximum in each iteration
        res = 1 # since curr is always a "good" node
        currMax = root.val

        def dfs(root, currMax):
            nonlocal res # because res is a global variable
            # base case
            if not root:
                return

            if root.val >= currMax:
                res += 1
                currMax = root.val
            