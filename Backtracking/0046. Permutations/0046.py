class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # basically recursively swap vals
        def backtrack(i):
