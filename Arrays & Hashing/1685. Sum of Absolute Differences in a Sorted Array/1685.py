class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        A = 0
        B = sum(nums)

        ans = [0] * n

        for i, x in enumerate(nums):
            ans[i] = (i - (n - i)) * x + B - A
            A += x
            B -= x

        return ans 