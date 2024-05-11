class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        wageQuality=[]
        for i in range(len(wage)):
            wageQuality.append((wage[i]/quality[i],quality[i]))
        wageQuality.sort()
        res=float('inf')
        currQuality=0

        maxHeap=[]

        for i in range(len(wageQuality)):
            if len(maxHeap)==k:
                currQuality-=abs(maxHeap[0])
                heapq.heappop(maxHeap)
            
            currQuality+=wageQuality[i][1]
            heapq.heappush(maxHeap,(-wageQuality[i][1]))
            if len(maxHeap)==k:
                res=min(res,wageQuality[i][0]*currQuality)

        return res
