# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd = even = 0
        curr = head
        while curr:
            if curr.val > curr.next.val:
                even += 1
            else:
                odd += 1
            curr = curr.next.next
        
        if odd == even:
            return "Tie"
        else:
            if odd > even:
                return "Odd"
            else:
                return "Even"