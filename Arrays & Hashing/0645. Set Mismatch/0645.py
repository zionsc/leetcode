class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lst = [0 for _ in range(len(nums) + 1)]
        missing = 0
        dup = 0

        for num in nums:
            lst[num] += 1

        for i,v in enumerate(lst):
            if v == 0:
                missing = i
            if v == 2:
                dup = i
                
            
        return [dup, missing]