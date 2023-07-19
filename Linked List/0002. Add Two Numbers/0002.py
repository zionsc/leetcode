# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # pattern: create dummy node, return dummy.next
        dummy = ListNode()
        curr = dummy

        # continue for or carry as well because of 8 + 7 -> then carry is 1, but then we forget about carry!
        carry = 0
        while l1 or l2 or carry:


        
        return dummy.next