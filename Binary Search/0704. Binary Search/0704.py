class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        return self.binarysearch(nums, target, l, r)

    def binarysearch(self, nums, target, l, right):
        if right >= left:
            mid = l + ((r - l) // 2)