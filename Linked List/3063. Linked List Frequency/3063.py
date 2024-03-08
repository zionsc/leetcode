# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = defaultdict(int)
        curr = head
        while curr:
            freq[curr.val] += 1
            curr = curr.next
        
        dummy = ListNode()
        curr = dummy
        for i,v in freq.items():
            new_node = ListNode(v, None)
            curr.next = new_node
            curr = curr.next

        return dummy.next