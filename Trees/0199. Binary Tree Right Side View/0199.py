# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        q.append(root)

        while q: # level-order traversal
            for i in range(len(q)): # per level
                node = q.popleft() # pop LEFT! -> pops until most very right (which is our rightmost node at that level)