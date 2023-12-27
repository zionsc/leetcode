class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        l,r = 0,1

        while r < len(colors):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                    r += 1
                else:
                    res += neededTime[r]
                    r += 1
            else:
                l = r
                r += 1
        return res