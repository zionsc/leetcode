"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        stack = []
        dummy = Node(0,None,head,None)
        stack.append(head)
        prev = dummy

        while stack:
            node = stack.pop()

            node.prev = prev
            prev.next = node

            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None
            
            prev = node

        dummy.next.prev = None
        return dummy.next