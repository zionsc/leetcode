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
        # cache will hold keys that point to nodes -> linkedlist
        self.cache = {}
        self.cap = capacity
        # basically left and right are going to pointers to the dummy nodes that start and finish the linkedlist.
        self.left, self.right = ListNode(0, 0), ListNode(0, 0) # initialize the dummy nodes for left and right
        self.left.next = self.right
        self.right.prev = self.left


    # to insert into the linkedList
    def insert(self, node):
        # adding to the prev of self.right (since self.right is a dummy node, the one prev to it is the MRU)
        # MRU -> most recently used key in cache (listnode)
        prev, next = self.right.prev, self.right

        # updaing the linked list pointers! 
        prev.next = node
        next.prev = node
        node.next = self.right
        node.prev = prev

    
    # to remove from the linkedlist
    def remove(self, node):
        prev, next = self.left, self.left.next

        # updating the linked list pointers



    def get(self, key: int) -> int:
        # implement
        if key in self.cache: # must use self.remove if calling class function inside of funct.
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # implement
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(self.cache[key])
        # updates the value to the new listNode -> else creates it and puts it in -> maps the key to the node's key
        # in order to access hashmap in O(1)
        self.cache[key] = ListNode(key, value)

        # must also check if it is larger than the cache -> if it is, then remove LRU
        if len(self.cache) > self.cap:
            # since self.left is the dummynode -> next is the LRU
            lru = self.left.next

            # remove from linkedlist
            self.remove(lru) # or self.remove(self.cache[lru.key]) -> does the same thing:
            # accessing linkedlist directly, or accessing linkedlist through the hashmap (cache)

            # remove from hashmap
            # each node has a key that maps to the hashmap
            del self.cache[lru.key]
            
