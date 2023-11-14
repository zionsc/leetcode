class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_map = Counter(nums)
        for i, v in my_map.items():
            if v > len(nums) // 2:
                return i
        
        