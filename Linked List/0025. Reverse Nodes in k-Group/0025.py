# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # basic idea is to iterate until kth node does not exist -> reverse them is the issue, but that's simply
        # messing around with pointers -> use a helperfunct to find kthnode

        dummy = ListNode(0, head)

        # must keep track of the prev node before the group to reverse as we need to update the pointers
        # in order to continue the linkedlist
        groupPrev = dummy

        while True:
            
    
    def findKth(self, currNode, k):
        # find the kth node -> easy
        while currNode and k > 0:
            currNode = currNode.next
            k -= 1
        return currNode
