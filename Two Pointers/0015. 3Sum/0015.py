class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # using the idea of sorting, we can make sure that a l and r pointer can be used to solve in O(n^2)

        for i, a in enumerate(nums):
            # since nums is sorted, if a == nums[i - 1], it is a repeat, thus skip.
            if i > 0 and a == nums[i - 1]: 
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # Both l and r have to change values as if one changes, it could be a duplicate.
                    l += 1
                    r -= 1

                    # increment l until it is not the same value as the previous l --> to avoid duplicates
                    # Find all the other subsets that include a that are not duplicates.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
