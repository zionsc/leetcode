class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n=len(ring)

        idxMap=defaultdict(list)
        for i,c in enumerate(ring):
            idxMap[c].append(i)

        dp=[[float('inf')]*n for _ in range(len(key))]
        for idx in idxMap[key[0]]:
            dp[0][idx]=min(idx,n-idx)+1
        
        for i in range(1,len(key)):
            for j in idxMap[key[i]]:
                for k in idxMap[key[i-1]]:
                    dist=abs(j-k)
                    minSteps=(dist,n-dist)
                    dp[i][j]=min(dp[i][j],dp[i-1][k]+minSteps+1)
        
        return min(dp[len(key)-1])
