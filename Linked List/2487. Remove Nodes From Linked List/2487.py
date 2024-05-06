# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        curr=prev
        while curr:
            while curr.next and curr.val>curr.next.val:
                curr.next=curr.next.next
            curr=curr.next
        
        curr=prev
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        return prev
