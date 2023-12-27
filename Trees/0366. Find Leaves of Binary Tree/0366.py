class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaf_levels = defaultdict(list)

        def dfs(node: Optonal[TreeNode]) -> int:
            if not node:
                return -1
            
            level = max(dfs(node.left), dfs(node.right)) + 1

            leaf_levels[level].append(node.val)

            return level
        
        dfs(root)
        return leaf_levels.values()