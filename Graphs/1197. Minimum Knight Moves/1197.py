class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        res = 0

        directions = [[2,1],[1,2],[-2,1],[1,-2],[-1,2],[2,-1],[-2,-1],[-1,-2]]

        visited = set()
        visited.add((0,0))
        queue = deque()
        queue.append((0,0))

        while queue:
            for _ in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                if curr_x == x and curr_y == y:
                    return res
                for dx, dy in directions:
                    new_x, new_y = curr_x + dx, curr_y + dy
                    if (new_x, new_y) not in visited:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
            res += 1
        
        return res
