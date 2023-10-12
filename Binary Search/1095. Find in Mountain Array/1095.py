# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Find peak of the mountain
        l, r = 0, mountain_arr.length() - 1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        
        # Binary search on the ascending part of the mountain
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) == target:
                return mid  # return the index immediately if found in ascending part
            elif mountain_arr.get(mid) < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # Binary search on the descending part of the mountain
        l, r = peak + 1, mountain_arr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) == target:
                return mid  # return the index if found in descending part
            elif mountain_arr.get(mid) > target:
                l = mid + 1
            else:
                r = mid - 1
        
        # If we haven't returned by this point, target isn't in the array
        return -1


        