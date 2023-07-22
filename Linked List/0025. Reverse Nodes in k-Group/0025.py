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
            kth = self.findKth(groupPrev.next, k)

            # if kth is out of bounds -> nothing happens
            if not kth:
                break
            
            # keep track of node: before the group and after the group
            groupNext = kth.next


            # reverse the group
            # in order to reverse the group, but still keep it connected, we must set prev to something other
            # than None
            prev, curr = kth.next, groupPrev.next
            # can't do while curr != None because we are reversing groups, but the entire linkedlist at once.
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            

            # now we must connect the new end of the linkedlist to the next node after the group in the linkedlist
            # in order to maintain a connected linkedlist

            # we must also update groupPrev for the next iteration of group -> it was the start node of the group 
            # before being reversed
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = groupPrev.next


        return dummy.next

            
    
    def findKth(self, currNode, k):
        # find the kth node -> easy
        while currNode and k > 0:
            currNode = currNode.next
            k -= 1
        return currNode
