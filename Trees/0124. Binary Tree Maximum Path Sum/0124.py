class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Define a helper function to calculate the maximum path sum with a given node as the root
        def dfs(node):
            nonlocal res  # Use the res variable from the outer function (maxPathSum)
            if not node:
                return 0

            # Get the maximum sum for the left and right subtrees (ignore negative sums)
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            # Uspdate the result with the maximum path sum that goes through the current node
            res = max(res, node.val + left_sum + right_sum) # need to return max of res, or possible split in tree 

            # Return the maximum sum that can be extended upwards (including the current node's value)
            return node.val + max(left_sum, right_sum)

            # need to update res -> result val to make sure it returns max possible, but need to return node.val + max(left, right) in order to tell next node up what its value currently is. 

        res = float('-inf')  # Initialize the result to negative infinity
        dfs(root)  # Start the recursive traversal

        return res
