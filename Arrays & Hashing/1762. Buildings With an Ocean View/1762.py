class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        tallest = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > tallest:
                res.append(i)
            tallest = max(tallest, heights[i])
        return reversed(res)