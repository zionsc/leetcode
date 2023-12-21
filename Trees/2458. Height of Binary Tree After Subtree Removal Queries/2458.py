# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth_map = defaultdict(int)
        height_map = defaultdict(int)

        def dfs(node, depth):
            if not node:
                return -1
            curr = 1 + max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
            depth_map[node.val] = depth
            height_map[node.val] = curr
            return curr

        dfs(root, 0)

        depth_to_node = defaultdict(list)
        for node, depth in depth_map.items():
            depth_to_node[depth].append((height_map[node], node))
            depth_to_node[depth].sort(reverse=True)
            if len(depth_to_node[depth]) > 2:
                depth_to_node[depth].pop()

        res = []
        for query in queries:
            depth = depth_map[query]
            if len(depth_to_node[depth]) == 1:
                res.append(depth - 1)
            elif depth_to_node[depth][0][1] == query:
                res.append(depth_to_node[depth][1][0] + depth)
            else:
                res.append(depth_to_node[depth][0][0] + depth)
        return res