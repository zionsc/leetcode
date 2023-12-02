class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            self.res = max(self.res, node.val, left + node.val + right)

            return max(node.val, node.val + left, node.val + right)

        dfs(root)
        return self.res