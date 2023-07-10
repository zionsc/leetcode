class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid

            # left-side is sorted (strictly increasing)
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: # must be in right-side -> greater than mid or less than l
                    l = mid + 1
                else:
                    r = mid - 1

            # right-side is sorted (strictly increasing)
            else:
                if target < nums[mid] or target > nums[r]: # must be in left-side -> less than mid or greater than r
                    r = mid - 1
                else:
                    l = mid + 1
            
            return -1 


