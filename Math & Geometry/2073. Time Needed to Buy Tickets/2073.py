class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res=0
        for i,v in enumerate(tickets):
            if i<=k:
                res+=min(tickets[i],tickets[k])
            else:
                res+=min(tickets[i],tickets[k]-1)
        return res
        