# the basic idea is to use a hashmap to have access to certain values in O(1) constant time
# to remove the least recently used value from our cache, we can simply just a linked list -> 
# the left most node would be LRU, the right-most node would be the most recently used node. need to update
# for each call.

# Implement a struct ListNode():
class ListNode:
    # the reason for key value is to make sure that we can access the hashmap from the node itself.
    def __init__(self, key, value):  
        self.key, self.val = key, value
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        # implement
        pass


    # to insert into the linkedList
    def insert(self, node):
    
    # to remove from the linkedlist
    def remove(self, node):


    def get(self, key: int) -> int:
        # implement
        pass

    def put(self, key: int, value: int) -> None:
        # implement
        pass
