# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete_set = set(to_delete)
        res = []

        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in delete_set:
                if not node.left and not node.right:
                    return None
                else:
                    if node.left:
                        res.append(node.left)
                    if node.right:
                        res.append(node.right)
                return None
            return node
        
        node = dfs(root)
        if node:
            res.append(node)
        return res