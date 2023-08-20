"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if not node:
                return
            
            # if already has been copied, no need to make a new copy
            if node in oldToNew:
                return oldToNew[node]
            
            # create a copy
            copy = Node(node.val)
            oldToNew[node] = copy

            for neigh in neighbors:
                # recursive leap of faith
                copy.neighbors.append(dfs(neigh))

            return copy
        
        newNode = dfs(node)
        return newNode
            
