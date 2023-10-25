# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()
            if level == len(res):
                res.append(node.val)
            else:
                res[level] = max(res[level], node.val)

            if node.left:
                queue.append((node, level + 1))
            if node.right:
                queue.append((node, level + 1))
            
        return res