class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = defaultdict(int)
        for num in nums:
            row = count[num]
            if row == len(res):
                res.append([])
            res[row].append(num)
            count[num] += 1
        return res