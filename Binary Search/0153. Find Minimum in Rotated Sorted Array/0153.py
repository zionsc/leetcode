class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # set currMin to initial inf value
        currMin = float("int")

        while l < r:
            mid = l + ((r - l) // 2)
            currMin = min(currMin, nums[mid])

            # start of sequence is at the right subarray
            if nums[mid] > nums[r]:
                l = mid + 1
            
            # start of sequence is at left subarray
            else:
                r = mid - 1

        currMin = min(currMin, nums[mid])
        return currMin