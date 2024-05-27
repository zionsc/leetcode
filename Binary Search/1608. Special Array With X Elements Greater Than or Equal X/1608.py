class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        l,r=0,n

        def bisectleft(target):
            l,r=0,n

            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid
                elif nums[mid] < target:
                    l = mid + 1
            return l
        
        while l <= r:
            mid = (l + r) // 2
            pos = bisect_left(nums, mid)
            # pos = bisectleft(mid)
            count = n - pos

            if count == mid:
                return mid
            elif count > mid:
                l = mid + 1
            elif count < mid:
                r = mid - 1
        
        return -1