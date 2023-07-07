class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        return self.binarysearch(nums, target, l, r)

    def binarysearch(self, nums, target, l, right):
        # make sure it does not go out of bounds
        if right >= left:
            mid = l + ((r - l) // 2)

            # base case
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binarysearch(nums, target, mid + 1, r)
            else: # nums[mid] > target
                return self.binarysearch(nums, target, l, mid - 1)
            
            # if not found
        return -1