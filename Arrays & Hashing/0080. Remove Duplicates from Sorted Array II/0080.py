class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        my_map = Counter(nums)
        for i in range(len(nums)):
            if my_map[nums[i]] > 2:
                my_map[nums[i]] -= 1
                continue
            res.append(nums[i])
        
        nums.clear()
        nums.extend(res)
                
                