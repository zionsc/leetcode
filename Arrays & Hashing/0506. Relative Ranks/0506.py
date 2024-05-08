class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        temp=[(v,i) for i,v in enumerate(score)]
        temp.sort(reverse=True)
        res=[""]*n

        for i in range(n):
            if(i==0):
                res[temp[i][1]]="Gold Medal"
            elif(i==1):
                res[temp[i][1]]="Silver Medal"
            elif(i==2):
                res[temp[i][1]]="Bronze Medal"
            else:
                res[temp[i][1]]=str(i+1)

        return res