class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # basically find the cycle first, then have two pointers take one step at a time, essentially making sure
        # that if the two pointers are the same number, then that is a duplicate because they will never
        # be the same index -> as they are both taking one step at a time at different locations.
        # the distance from 0 to the start of the cycle and the distance from the index that the the cycle
        # algorithm found to the start of the cycle is the same, thus meaning that if they both take one step at
        # a time, then they will both point to the start of the cycle at the same time, meaning that they will be
        # duplicate numbers at different indexes (since they point to the same index) 