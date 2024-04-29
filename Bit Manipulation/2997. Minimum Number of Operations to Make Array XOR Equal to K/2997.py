class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr=0
        for num in nums:
            curr^=num
        curr^=k
        return bin(curr).count('1')