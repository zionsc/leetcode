class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + (r - l) // 2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return left

        # def binarysearch(left, right):
        #     if left > right:
        #         return left
        #     mid = (left + (right - left) // 2)
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     return binarysearch(left, right)
        
        # return binarysearch(0, len(nums) - 1)
            