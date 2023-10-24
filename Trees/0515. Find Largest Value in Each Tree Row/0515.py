# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # my_map = defaultdict(list)
        # res = []

        # def dfs(node, idx):
        #     if not node:
        #         return
        #     my_map[idx].append(node.val)
        #     dfs(node.left, idx + 1)
        #     dfs(node.right, idx + 1)
            
        # dfs(root, 0)
        # for k,v in my_map.items():
        #     res.append(max(v))
        # return res

        if not root:
            return []

        res = []
        queue = deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()

            if level == len(res): # it is a new level
                res.append(node.val)
            else: # existing level
                res[level] = max(res[level], node.val)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return res







        