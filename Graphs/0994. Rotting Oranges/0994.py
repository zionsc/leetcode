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

        while q and fresh > 0: # will stop at either point, both must be true
            for i in range(len(q)): # for all items in the queue

                r, c = q.popleft() # does not change the iteration in the for i in range(len(q))

                for dr, dc in directions:
                    if r + dr in range(rows) and c + dc in range(cols) and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        q.append([r + dr, c + dc])
                        fresh -= 1
                
            time += 1 # outside of the q, since each time q loop iterates, that is one time unit. 

        return time if fresh == 0 else -1 # return the time if no more fresh. else if there is still fresh, not possible, thus return -1. 

