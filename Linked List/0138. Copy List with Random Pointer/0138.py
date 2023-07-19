"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if the old one is none, it should create a copy as none as well. 
        oldToCopy = { None: None }

        # first iteration to create the deepcopy
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] 