class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        n = len(costs) // 2

        res = 0
        for a,b in costs:
            refund.append(b - a)
            res += a
        
        refund.sort(key=lambda x:(x))
        for i in range(n):
            res += refund[i]
        
        return res