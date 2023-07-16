# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # for empty linked lists
        if not head:
            return None
        
        # we need to go backwards, but we also need to keep track of head.next! 
        newHead = head
        if head.next:
            # go through to the end until the last value
            newHead = self.reverseList(head.next)
            # make head's next value point point to itself, essentially reversing that part of the linked list
            head.next.next = head

        # basically making sure that our current pointer does not point to the original next value (we must delete old next pointers as well)
        head.next = None
        # the head of the new linked list as newHead stays as the last value
        return newHead

