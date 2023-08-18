class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        # basically we want to iterate through each [row][col] to see if it has been marked by bfs
        rows, cols = len(grid), len(grid[0])
        visited = set()

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
        
        
