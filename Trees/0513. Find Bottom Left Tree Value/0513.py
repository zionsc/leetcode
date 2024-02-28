# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res = [-1, float('inf')]

        def dfs(node, level):
            if not node:
                return
            if level < self.res[1]:
                self.res = [node.val, level]
            
            dfs(node.left, level - 1)
            dfs(node.right, level - 1)
        
        dfs(root, 0)
        return self.res[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
#         res = [0,float('inf')]
#         queue = deque([(root, 0)])
#         while queue:
#             node,level = queue.popleft()
#             if not node.left and not node.right and level < res[1]:
#                 res = [node.val, level]
#             if node.left:
#                 queue.append((node.left, level - 1))
#             if node.right:
#                 queue.append((node.right, level - 1))
#         return res[0]
        