class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # basically find the cycle first, then have two pointers take one step at a time, essentially making sure
        # that if the two pointers are the same number, then that is a duplicate because they will never
        # be the same index -> as they are both taking one step at a time at different locations.
        # the distance from 0 to the start of the cycle and the distance from the index that the the cycle
        # algorithm found to the start of the cycle is the same, thus meaning that if they both take one step at
        # a time, then they will both point to the start of the cycle at the same time, meaning that they will be
        # duplicate numbers at different indexes (since they point to the same index) 
        # must understand that values in the array are also indexes because it says values are from 1 ot n-1

        # step 1: cycle detection
        slow, fast = 0, 0
        while True:
            slow = nums[slow] # taking one step at a time
            fast = nums[nums[fast]] # taking two steps at once
            if slow == fast:
                break
        

        # step 2: find the duplicate by taking one step at a time from c-x and p.
        # they will both eventually go into the start of the cycle. -> because literally they have to
        slow2 = 0
        while True:
            # distance from start -> start of cycle == cycle detection -> start of cycle
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow # we return the value (it is also the index of the start of the cycle)
        
