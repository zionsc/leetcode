# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
    # basic idea is to make a helper function that merges two lists -> merge two lists at a time until only one list left
        if not lists or len(lists) == 0:
            return None
        
        
    


    def mergeLists(self, l1, l2):
        # implement
        pass