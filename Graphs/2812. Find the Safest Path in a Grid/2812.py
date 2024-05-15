class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)
        distance=[[-1]*n for _ in range(n)]
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        q=deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j,0))
        
        while q:
            r,c,dist=q.popleft()
            if distance[r][c]!=-1:
                continue
            distance[r][c]=dist
            for dx,dy in directions:
                if 0<=r+dx<n and 0<=c+dy<n:
                    q.append((r+dx,c+dy,dist+1))
        
        pq=[(-distance[0][0],0,0)]
        visited=set()
        while pq:
            dist,r,c=heapq.heappop(pq)
            dist=-dist
            if r==n-1 and c==n-1:
                return dist
            for dx,dy in directions:
                if 0<=r+dx<n and 0<=c+dy<n and (r+dx,c+dy) not in visited and grid[r+dx][c+dy]!=1:
                    new_dist=distance[r+dx][c+dy]
                    heapq.heappush(pq,(-min(dist,new_dist),r+dx,c+dy))
                    visited.add((r+dx,c+dy))
        
        return 0