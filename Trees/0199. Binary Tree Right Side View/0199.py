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
            rightSide = None
            for i in range(len(q)): # per level
                node = q.popleft() # pop LEFT! -> pops until most very right (which is our rightmost node at that level)
                if node:
                    # order of append is important to make sure right is the rightmode in the q not the leftmost!
                    q.append(node.left)
                    q.append(node.right)
                    rightSide = node
            if rightSide:
                res.append(rightSide.val)
                
        
        return res
            