# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, freq):
            if not node:
                self.res += 1 if sum(v % 2 == 1 for v in freq.values()) <= 1 else 0
                return
            
            freq[node.val] = freq.get(node.val, 0) + 1

            if node.left and node.right:
                dfs(node.left, freq)
                dfs(node.right, freq)
            elif node.left:
                dfs(node.left, freq)
            elif node.right:
                dfs(node.right, freq)
            else:
                dfs(node.left, freq)
            
            freq[node.val] -= 1
            if freq[node.val] == 0:
                del freq[node.val]
            
        dfs(root, {})
        return self.res
                
