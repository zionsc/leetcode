class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        s=res=0
        i=len(happiness)-1
        happiness.sort()
        while k>0 and i>=0:
            res+=happiness[i]-s if happiness[i]-s>=0 else 0
            s+=1
            k-=1
            i-=1
        return res