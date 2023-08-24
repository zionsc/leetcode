class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        time, fresh = 0, 0

        # basic idea is because we may have more than one rotten orange, they will start making the fresh ones rotten at the same time! -> reason for queue instead
        # of simple BFS.

        # first finding the number of fresh oranges (if not connected to the group that contains rotten, we cannot get every orange rotten!)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # fresh
                    fresh += 1
                elif grid[r][c] == 2: # rotten
                    q.append([r, c])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        