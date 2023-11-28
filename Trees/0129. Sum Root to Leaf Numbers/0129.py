    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def sumNumbers(self, root: Optional[TreeNode]) -> int:
            self.res = 0
            def dfs(node, numString):
                if not node:
                    return
                if not node.left and not node.right:
                    numString += str(node.val)
                    self.res += int(numString)
                    return
                numString += str(node.val)
                dfs(node.left, numString)
                dfs(node.right, numString)

            dfs(root, "")
            return self.res