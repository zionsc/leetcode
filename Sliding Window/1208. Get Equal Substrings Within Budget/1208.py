class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs=[abs(ord(s_v)-ord(t_v)) for s_v,t_v in zip(s,t)]
        res=0
        l=curr=0
        for r in range(len(s)):
            maxCost-=costs[r]
            curr+=1
            if (maxCost>=0):
                res=max(res,curr)
            while (maxCost<0):
                curr-=1
                maxCost+=costs[l]
                l+=1
            
        return res