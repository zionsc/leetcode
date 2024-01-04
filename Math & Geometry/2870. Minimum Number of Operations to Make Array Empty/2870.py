class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        nums_map = Counter(nums)
        for i,v in nums_map.items():
            if v == 1:
                return -1
            res += v // 3
            if v % 3:
                res += 1
        return res
            
            