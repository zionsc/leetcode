# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # basically BFS iteratively

        q = collections.deque()
        res = []

        # to initialize q
        q.append(root)

        while q:
            
