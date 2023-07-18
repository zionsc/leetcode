class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # step one: find the two halves of the linkedlist
        slow, fast = head, head.next
        while fast and fast.next: # until fast and fast.next is out of bounds
            slow = slow.next
            fast = fast.next.next
        

        secondHalf = slow.next
        slow.next = None