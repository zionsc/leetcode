class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(v for i,v in freq.items())
        res = 0
        for i,v in freq.items():
            if v == max_freq:
                res += max_freq
        return res