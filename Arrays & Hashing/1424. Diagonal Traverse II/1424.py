class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = defaultdict(deque)
        for i, rows in enumerate(nums):
            for j, val in enumerate(nums[i]):
                res[i + j].appendleft(val)

        return chain(*res.values())