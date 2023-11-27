# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val: # check to see if it is the start of a duplicates sequence
                while head.next and head.val == head.next.val: # loop to remove the duplicates
                    head = head.next
                prev.next = head.next # since the loop doesn't account for the last duplicate

            else: 
                prev = prev.next

            head = head.next # increment head 
        
        return dummy.next