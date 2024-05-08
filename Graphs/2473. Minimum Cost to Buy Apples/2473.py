class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        adjList=defaultdict(list)
        for u,v,w in roads:
            adjList[u-1].append((v-1,w))
            adjList[v-1].append((u-1,w))

        res=[float('inf') for _ in range(n)]
        for i in range(n):
            dist=[float('inf') for _ in range(n)]
            dist[i]=0
            pq=[(0,i)]
            while pq:
                nodeCost,node=heapq.heappop(pq)
                res[i]=min(res[i], appleCost[node]+(k+1)*nodeCost)
                for nei,neiCost in adjList[node]:
                    if neiCost+nodeCost<dist[nei]:
                        dist[nei]=neiCost+nodeCost
                        heapq.heappush(pq, (neiCost+nodeCost,nei))
        
        return res
