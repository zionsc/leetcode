class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        # basically we want to iterate through each [row][col] to see if it has been marked by bfs
        rows, cols = len(grid), len(grid[0])
        visited = set()
        numIslands = 0

        # basic BFS
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))
            
            while queue:
                row, col = queue.popleft()
                neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in neighbours:
                    if (row + dr) in range(r) and (col + dc) in range(c) and grid[row + dr][col + dc] == "1" and (row + dr, col + dc) not in visited:
                        visited.add((row + dr, col + dc))
                        queue.append((row + dr, col + dc))
        

        # now check each possible [row][col]
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    numIslands += 1

        return numIslands
