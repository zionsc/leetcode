from typing import List
import collections

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        if not rooms or not rooms[0]:  # Added to handle empty input
            return rooms
            
        rows, cols = len(rooms), len(rooms[0])
        gates = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    gates.append((r, c, 0))  # Store distance too

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while gates:
            r, c, curr_distance = gates.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] != -1:
                    new_distance = curr_distance + 1
                    if rooms[nr][nc] > new_distance:  # Check if new distance is less than existing distance
                        rooms[nr][nc] = new_distance
                        gates.append((nr, nc, new_distance))

        return rooms
