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