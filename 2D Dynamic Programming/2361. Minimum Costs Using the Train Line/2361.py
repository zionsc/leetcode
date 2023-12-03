class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        dp1, dp2 = regular[0], express[0] + expressCost
        res = [min(dp1, dp2)] # initialize where we want to start initially

        for i in range(1, len(regular)):
            dp1t = dp1
            dp1 = min(dp1 + regular[i], dp2 + regular[i])
            dp2 = min(dp1t + express[i] + expressCost, dp2 + express[i])
            res.append(min(dp1, dp2))
        
        return res