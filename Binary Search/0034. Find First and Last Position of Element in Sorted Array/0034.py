class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            pass
        
        def findRight(nums, target):
            pass

        left, right = findLeft(nums, target), findRight(nums, target)

        return [left, right] if left <= right else [-1, -1]
