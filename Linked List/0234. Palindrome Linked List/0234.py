# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = head
        prev = None
        while curr != slow:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != prev.val:
                return False
            else:
                slow = slow.next
                prev = prev.next
        return True