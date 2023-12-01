class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        res = 0

        directions = [[2,1],[1,2],[-2,1],[1,-2],[-1,2],[2,-1],[-2,-1],[-1,-2]]

        visited = set()
        visited.add((0,0))
        queue = deque()
        queue.add((0,0))

        while queue: