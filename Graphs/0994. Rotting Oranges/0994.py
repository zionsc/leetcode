class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        time, fresh = 0, 0

        # basic idea is because we may have more than one rotten orange, they will start making the fresh ones rotten at the same time! -> reason for queue instead
        # of simple BFS.