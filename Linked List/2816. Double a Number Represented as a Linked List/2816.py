# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        curr=prev
        prev2=None
        carry=0
        while(curr):
            val=curr.val*2
            val+=carry
            curr.val=val%10
            carry=val//10
            prev2=curr
            curr=curr.next
        
        if(carry):
            newNode=ListNode(carry)
            prev2.next=newNode
        
        curr=prev
        prev=None
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        return prev