# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # initialize these pointers (because or else it would edit the linked list values)
        prev, curr = None, head

        # basic logic, just update the pointers. curr, curr.next, prev, temp are all POINTERS. NOT NODES THEMSELVES.
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev