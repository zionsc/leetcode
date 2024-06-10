class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        for v1, v2 in zip(heights, sorted(heights)):
            if v1 != v2:
                res += 1
        return res