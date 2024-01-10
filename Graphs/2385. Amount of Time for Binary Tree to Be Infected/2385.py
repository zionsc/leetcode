# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj_list = defaultdict(list)

        def make_graph(node):
            if not node:
                return 
            if node.left:
                adj_list[node.val].append(node.left.val)
                adj_list[node.left.val].append(node.val)
            if node.right:
                adj_list[node.val].append(node.right.val)
                adj_list[node.right.val].append(node.val)
            make_graph(node.left)
            make_graph(node.right)
        
        make_graph(root)

        queue = deque([(start)])
        visited = set()
        visited.add(start)
        res = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for nei in adj_list[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            if queue:
                res += 1
            
        return res
        