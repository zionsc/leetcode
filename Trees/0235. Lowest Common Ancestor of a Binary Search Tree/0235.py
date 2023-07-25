# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # basically the LCA is where the split happens between left and right -> for obvious reasons that has to be the lowest common ancestor.
        curr = root

        while curr:
            if curr.val > p.val and curr.val > q.val: # switch curr to curr.left because both p and q fall under curr.left as the ancestor
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr
