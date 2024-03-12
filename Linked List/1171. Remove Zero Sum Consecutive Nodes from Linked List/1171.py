# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        sum_allocation = {0:dummy}
        prefix = 0

        while head:
            prefix += head.val
            sum_allocation[prefix] = head
            head = head.next
        
        prefix = 0
        head = dummy

        while head:
            prefix += head.val
            head.next = sum_allocation[prefix].next
            head = head.next
        
        return dummy.next
