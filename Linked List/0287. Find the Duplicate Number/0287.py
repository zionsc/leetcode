class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # basically find the cycle first, then have two pointers take one step at a time, essentially making sure
        # that if the two pointers are the same number, then that is a duplicate because they will never
        # be the same index -> as they are both taking one step at a time at different locations.