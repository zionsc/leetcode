class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        adjList=defaultdict(list)
        for u,v,w in roads:
            adjList[u-1].append((v-1,w))
            adjList[v-1].append((u-1,w))

        res=[appleCost[i] for i in range(n)]
        q=[(cost,start) for start,cost in enumerate(appleCost)]

        while q:
            currCost,currNode=heapq.heappop(q)
            if currCost>res[currNode]:
                continue
            for nei,neiCost in adjList[currNode]:
                if res[nei]>res[currNode]+(k+1)*neiCost:
                    res[nei]=res[currNode]+(k+1)*neiCost
                    heapq.heappush(q,(res[nei],nei))
        return res

