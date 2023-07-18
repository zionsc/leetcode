class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # step one: find the two halves of the linkedlist
        slow, fast = head, head.next
        while fast and fast.next: # until fast and fast.next is out of bounds
            slow = slow.next
            fast = fast.next.next
        

        # second half of the list starts at slow.next and then slow should point to nullptr in order to separate the lists -> this all works with pointers
        secondHalf = slow.next
        slow.next = None

        # step two: reverse the second half of the list in order to iterate through the second half of the list backwards! 
        prev = None
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp

        # step three: merge the the separated lists into one!
        firstHalf = head
        secondHalf = prev # make it the start of the secondHalf
        while firstHalf and secondHalf:
            tmp1, tmp2 = firstHalf.next, secondHalf.next # keep these in a pointer because we need to access them after we change the pointers
            firstHalf.next = secondHalf
            secondHalf.next = tmp1
            firstHalf, secondHalf = tmp1, tmp2
        
        