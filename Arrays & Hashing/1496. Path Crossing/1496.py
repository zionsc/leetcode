class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        curr = (0,0)
        visited.add(curr)
        for p in path:
            x,y = curr
            if p == 'N':
                curr = (x, y + 1)
            elif p == 'E':
                curr = (x + 1, y)
            elif p == 'S':
                curr = (x, y - 1)
            elif p == 'W':
                curr = (x - 1, y)
            if curr in visited:
                return True
            visited.add(curr)
            
        return False

