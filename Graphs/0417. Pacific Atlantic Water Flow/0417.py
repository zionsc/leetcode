class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set() # checking for each r, c if they are in both pac and atl
        res = []

        def dfs(r, c, visitSet, prevHeight):
            # since we are starting from the border values, we must check that heights[r][c] < prevHeight as the base case to stop the recursive tree (opposite thinking)
            if ((r, c) in visitSet or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight):
                return
            
            
            visitSet.add((r, c))

            # each recursive tree
            dfs(r + 1, c, visitSet, heights[r][c])
            dfs(r - 1, c, visitSet, heights[r][c])
            dfs(r, c + 1, visitSet, heights[r][c])
            dfs(r, c - 1, visitSet, heights[r][c])

        
        # top and bottom row -> borders pacific (top), borders atlantic (bottom)
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # left and right cols -> borders pacific (left), borders atlantic (right)
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        # now check if each r, c is in BOTH sets!
        for r in range(rows):
            for c in range(cols):
                if ((r, c) in pac and (r, c) in atl):
                    res.append([r, c])
        
        return res