"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_visited = set()
        while p:
            p_visited.add(p)
            p = p.parent
        while q:
            if q in p_visited:
                return q
            q = q.parent
        return None

        