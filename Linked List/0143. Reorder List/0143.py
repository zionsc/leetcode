class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # step one: find the two halves of the linkedlist
        slow, fast = head, head.next
        