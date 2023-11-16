class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        set_nums = set(int(num, 2) for num in nums)
        n = len(nums)
        for i in range(n + 1):
            if i not in set_nums:
                return bin(i)[2:].zfill(n)
        