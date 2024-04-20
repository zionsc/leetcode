class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        if not land:
            return []

        rows,cols=len(land),len(land[0])
        def bfs(r,c):
            br=[r,c]
            visited.add((r,c))
            q=deque([(r,c)])
            while q:
                curr_r,curr_c=q.popleft()
                for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                    if curr_r+dr in range(rows) and curr_c+dc in range(cols) and (curr_r+dr,curr_c+dc) not in visited and land[curr_r+dr][curr_c+dc]==1:
                        visited.add((curr_r+dr,curr_c+dc))
                        q.append((curr_r+dr,curr_c+dc))
                        if curr_r+dr>br[0] or (curr_r+dr==br[0] and curr_c+dc>br[1]):
                            br=[curr_r+dr,curr_c+dc]
            return br

        res=[]
        visited=set()
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and land[r][c]==1:
                    br=bfs(r,c)
                    res.append([r,c,br[0],br[1]])
        return res