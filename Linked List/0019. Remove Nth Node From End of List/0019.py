class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # set the dummy.next = head
        l = dummy
        r = head

        # iterate r to have n nodes between r and l
        while n > 0 and r:
            r = r.next
            n -=1
        
        # iterate until r goes out of bounds -> basically found the nth node from the end
        while r:
            l = l.next
            r = r.next

        # remove the nth node set l.next to the next.next value
        l.next = l.next.next

        # dummy.next is head
        return dummy.next

        