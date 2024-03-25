class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # res = []
        # for num in nums:
        #     idx = abs(nums) - 1
        #     if nums[idx] < 0:
        #         res.append(abs(nums))
        #     nums[idx] *= -1
        # return res
    
        res = [0] * (len(nums) + 1)
        for num in nums:
            res[num] += 1

        return [i for i in range(len(res)) if res[i] == 2]            
