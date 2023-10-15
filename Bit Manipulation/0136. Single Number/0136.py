class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # xor is communiative --> can rearrange 
        for n in nums:
            res ^= n
        return res