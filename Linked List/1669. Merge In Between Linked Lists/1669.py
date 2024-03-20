# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
            
        while (a-1):
            temp = temp.next
            a -= 1
            b -= 1

        temp2 = temp.next
        while b:
            temp2 = temp2.next
            b -= 1

        temp.next = list2

        curr = list2
        while curr.next:
            curr = curr.next
        
        curr.next = temp2
        return list1      
