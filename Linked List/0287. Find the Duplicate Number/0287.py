class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break # slow == fast, there is a cycle --> the reason we do this is to make sure we find any value first. 

        slow2 = 0
        while True: 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: # slow == slow2, then there are two values that are the same that are not at the same index
                return slow