# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy_less = ListNode()
        curr_less = dummy_less
        dummy_more = ListNode()
        curr_more = dummy_more

        curr = head
        while curr.next:
            if curr.val < x:
                curr_less.next = curr
                curr_less = curr_less
            else:
                curr_more.next = curr
                curr_more = curr_more.next
            curr = curr.next

        if curr:
            if curr.val < x:
                curr_less.next = curr
                curr_less = curr_less.next
            else:
                curr_more.next = curr
                curr_more = curr_more.next
            curr_less = None
            curr_more = None
        
        curr_less.next = dummy_more.next
        return dummy_less.next