class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # create a new node in case l1 and l2 do not exist, then we must just return an empty thing. Tail is simply a pointer to iterate
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # update the pointer (what tail points to, not what tail actually is)
            tail = tail.next
        
        # if one of the l1 or l2 still has values in it, can just smack our newlist to the start of the remaining ones (just because it is sorted)
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # because dummy.next would be nullptr if not changed with tail
        return dummy.next
