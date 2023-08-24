from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        rows, cols = len(rooms), len(rooms[0])
        gates = collections.deque()
        curr_distance = 0

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    gates.append((r, c))

        def bfs(r, c, curr_distance):
            if r in range(rows) and c in range(cols) and rooms[r][c] != -1):
                if rooms[r][c] != 0:
                    rooms[r][c] = min(rooms[r][c], curr_distance)

                directions[[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:  
                    bfs(r + dr, c + dc, curr_distance += 1)

            else:
                return

        while q:
            r, c = q.popleft()
            bfs(r, c, 0)

        return rooms






            



